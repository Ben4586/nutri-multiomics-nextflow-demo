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

workflow {
    micro = Channel.fromPath(params.microbiome)
    meta = Channel.fromPath(params.metabolomics)
    clinical = Channel.fromPath(params.clinical)

    INTEGRATE(micro, meta, clinical)

    MODEL(INTEGRATE.out)
}