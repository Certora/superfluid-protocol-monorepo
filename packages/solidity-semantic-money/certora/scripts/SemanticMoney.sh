if [[ "$1" ]]
then
    RULE="--rule $1"
fi
 
certoraRun \
    certora/harnesses/SemanticMoneyHarness.sol \
    --verify SemanticMoneyHarness:certora/specs/SemanticMoney.spec \
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
    --settings -showInternalFunctions \
    --msg "SemanticMoneyHarness: $1 $2"