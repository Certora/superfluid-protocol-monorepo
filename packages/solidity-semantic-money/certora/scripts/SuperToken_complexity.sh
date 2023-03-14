#!/bin/bash

# if test -n "$1"
# then
#     METHOD="--method $1"
# fi

# certoraRun certora/configs/Complexity.conf \
#     $METHOD \
#     --send_only \
#     --msg "ControllerHarness:Complexity.spec $1 -- $2" \

    # certora/helpers/DummyERC20A.sol \

if [[ "$1" ]]
then
    RULE="--rule $1"
fi

certoraRun \
    certora/harnesses/ToySuperTokenHarness.sol \
    certora/munged/ToySuperToken.sol:ToySuperTokenPool \
    certora/harnesses/SemanticMoneyHarness.sol \
    --verify ToySuperTokenHarness:certora/specs/complexity.spec \
    --packages @openzeppelin=../../node_modules/@openzeppelin @superfluid-finance/solidity-semantic-money/src=src \
    --staging \
    --optimistic_loop \
    --loop_iter 3 \
    --solc solc8.19 \
    $RULE \
    --send_only \
    --msg "SuperTokenHarness complexity: $1 $2"  