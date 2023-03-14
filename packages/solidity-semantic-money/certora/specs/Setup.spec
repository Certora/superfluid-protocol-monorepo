using SemanticMoneyHarness as semanticMoneyHarness

// methods {
//     add(uint32,uint32) returns (uint32) envfree
//     sub(uint32,uint32) returns (uint32) envfree 
//     add(semanticMoneyHarness.Value,semanticMoneyHarness.Value) returns (semanticMoneyHarness.Value) envfree
//     mul(semanticMoneyHarness.Value,semanticMoneyHarness.Unit) returns (semanticMoneyHarness.Value) envfree
//     // mul(int128,uint32) returns (int256) envfree
//     mul(semanticMoneyHarness.FlowRate,semanticMoneyHarness.Time) returns (semanticMoneyHarness.Value) envfree
//     mul(semanticMoneyHarness.FlowRate a, semanticMoneyHarness.Unit b) returns (semanticMoneyHarness.FlowRate) envfree => mulFU_sum(a, b)
//     mul_nn(semanticMoneyHarness.FlowRate,semanticMoneyHarness.Unit) returns (semanticMoneyHarness.FlowRate) envfree
//     // mul(int128,int128) returns (int128) envfree
//     mul_quotRem(semanticMoneyHarness.FlowRate,semanticMoneyHarness.Unit,semanticMoneyHarness.Unit) returns (semanticMoneyHarness.FlowRate, semanticMoneyHarness.FlowRate) envfree
//     quotRem(semanticMoneyHarness.FlowRate,semanticMoneyHarness.Unit) returns (semanticMoneyHarness.FlowRate,semanticMoneyHarness.FlowRate) envfree
//     // mul_quotRem(int128,uint128,uint128) returns (int128,int128) envfree
//     // rtb(uint32,int256,int128,uint32) returns (int256) envfree
//     // rtb((uint32,int256,int128),uint32) returns (int256) envfree
//     rtbBT(semanticMoneyHarness.BasicParticle,semanticMoneyHarness.Time) returns (semanticMoneyHarness.Value) envfree
// }
 