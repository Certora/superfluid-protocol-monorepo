using SemanticMoneyHarness as semanticMoneyHarness

methods {
    distriutor() returns (address) => DISPATCHER(true)
    getIndex() returns ((uint128,(uint32,int256,int128))) => DISPATCHER(true)
    setIndex(semanticMoneyHarness.PDPoolIndex) => DISPATCHER(true)
    // getMember(address) returns ((semanticMoneyHarness.Unit,semanticMoneyHarness.Value,semanticMoneyHarness.BasicParticle)) => DISPATCHER(true)
    getMember(address) returns ((int128,int256,(uint32,int256,int128))) => DISPATCHER(true)
    updatePoolMember(address, semanticMoneyHarness.Unit) returns (bool) => DISPATCHER(true)
    // getIndex() returns ((uint128,(uint32,int256,int128))) envfree
    // setIndex((uint128,(uint32,int256,int128))) envfree
    // getMember(address) returns ((uint128,int256,())) envfree
     // updatePoolMember(address, uint128,(uint32,int256,int128)) returns (bool) envfree
}


rule complexity_check {
    method f; env e; calldataarg args;

    f(e, args);

    assert false, "this assertion should fail";
} 