#!/bin/bash -ue
python /home/benteh/nutri-multiomics-nextflow-demo/scripts/integrate_data.py         --micro microbiome.csv         --meta metabolomics.csv         --clinical clinical.csv         --output integrated.csv
