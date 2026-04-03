nextflow.enable.dsl=2

process INTEGRATE {
    publishDir "results/", mode: 'copy'
    input:
    path micro
    path meta
    path clinical

    output:
    path "integrated.csv"

    script:
    """
    python ${projectDir}/scripts/integrate_data.py \
        --micro $micro \
        --meta $meta \
        --clinical $clinical \
        --output integrated.csv
    """
}

process MODEL {
    publishDir "results/", mode: 'copy'
    input:
    path integrated
    
    output:
    path "model.pkl"
    path "feature_importance.csv"

    script:
    """
    python ${projectDir}/scripts/predictive_model.py $integrated
    """
}

process COBRA_MODEL {
    publishDir "results/", mode: 'copy'

    output:
    path "cobra_fluxes.csv"

    script:
    """
    python ${projectDir}/scripts/cobra_simulation.py
    """
}

process ABM_MODEL {
    publishDir "results/", mode: 'copy'

    output:
    path "abm_simulation.csv"

    script:
    """
    python ${projectDir}/scripts/agent_based_model.py
    """
}

workflow {
    micro = Channel.fromPath(params.microbiome)
    meta = Channel.fromPath(params.metabolomics)
    clinical = Channel.fromPath(params.clinical)

    integrated = INTEGRATE(micro, meta, clinical)

    model_out = MODEL(integrated)

    // NEW modeling layers
    COBRA_MODEL()
    ABM_MODEL()
}