#!/bin/bash
export KMP_DUPLICATE_LIB_OK=TRUE
time neuralplexer-inference --task=batched_structure_sampling \
                       --input-receptor data/6cm4.pdb \
                       --input-ligand data/ChEBI_8356.sdf \
                       --use-template \
                       --input-template data/6cm4.pdb \
                       --out-path out/ \
                       --model-checkpoint ../checkpoints/complex_structure_prediction.ckpt \
                       --n-samples 16 \
                       --chunk-size 8 \
                       --num-steps=40 \
                       --confidence \
                       --sampler=langevin_simulated_annealing
