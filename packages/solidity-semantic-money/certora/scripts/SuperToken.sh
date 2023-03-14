if [[ "$1" ]]
then
    RULE="--rule $1"
fi

certoraRun \
    certora/harnesses/ToySuperTokenHarness.sol \
    certora/munged/ToySuperToken.sol:ToySuperTokenPool \
    --verify ToySuperTokenHarness:certora/specs/SuperToken.spec \
    --packages @openzeppelin=../../node_modules/@openzeppelin @superfluid-finance/solidity-semantic-money/src=src \
    --cloud \
    --optimistic_loop \
    --loop_iter 3 \
    --solc solc8.19 \
    --rule_sanity=basic \
    --settings -depth=60 \
    --settings -mediumTimeout=300 \
    --settings -t=1200 \ 
    $RULE \
    --send_only \
    --settings -multipleCEX=basic,-postProcessCEXTimeout=100,-multiAssertCheck \
    --msg "ToySuperTokenHarness: $1 $2"

     