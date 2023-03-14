import "Setup.spec"

methods {
    harness_mt_t_add_t(uint32,uint32) returns (uint32) envfree
    harness_mt_v_sub_v(semanticMoneyHarness.Value,semanticMoneyHarness.Value) returns (semanticMoneyHarness.Value) envfree
    harness_inv_v(semanticMoneyHarness.Value) returns (semanticMoneyHarness.Value) envfree   
    harness_mulFT(semanticMoneyHarness.FlowRate a, semanticMoneyHarness.Time b) returns (semanticMoneyHarness.Value) envfree // => mul_fu_cvl(a, b)
    harness_mulVU(semanticMoneyHarness.Value a, semanticMoneyHarness.Unit b) returns (semanticMoneyHarness.Value) envfree // => mul_fu_cvl(a, b)
    harness_mulFU(semanticMoneyHarness.FlowRate a, semanticMoneyHarness.Unit b) returns (semanticMoneyHarness.FlowRate) envfree // => mul_fu_cvl(a, b)
    mul(semanticMoneyHarness.FlowRate a, semanticMoneyHarness.Unit b) returns (semanticMoneyHarness.FlowRate) envfree => mul_fu_cvl(a, b)
    
    harness_divFU(semanticMoneyHarness.FlowRate a, semanticMoneyHarness.Unit b) returns (semanticMoneyHarness.FlowRate) envfree  => div_fu_cvl(a, b)
    // AdditionalMonetaryTypeHelpers.div(semanticMoneyHarness.FlowRate a, semanticMoneyHarness.Unit b) returns (semanticMoneyHarness.FlowRate) envfree => div_fu_cvl(a, b)
    harness_rtbBT(semanticMoneyHarness.BasicParticle,semanticMoneyHarness.Time) returns (semanticMoneyHarness.Value) envfree

    harness_clonePI(semanticMoneyHarness.PDPoolIndex) returns ((int128,(uint32,int256,int128))) envfree
    harness_pool_member_update(semanticMoneyHarness.PDPoolMemberMU, semanticMoneyHarness.BasicParticle, semanticMoneyHarness.Unit, semanticMoneyHarness.Time) returns ((int128,(uint32,int256,int128)), (int128,int256,(uint32,int256,int128)), (uint32,int256,int128)) envfree
}

ghost int128 mul_fu;
function mul_fu_cvl(semanticMoneyHarness.FlowRate a,semanticMoneyHarness.Unit b) returns semanticMoneyHarness.FlowRate {
	havoc mul_fu assuming ( 
        to_mathint(mul_fu@new) == to_mathint(a) * to_mathint(b)
	);
    return mul_fu;
}
// 15,6 => 2,3     (>=c*b  <(c+1)*b) 
// -15,-6 => 2,-3  (<=c*b, >(c+1)*b)
// 15,-6 => -2,3   (<=(c-1)*b,>=c*b)
// -15,6 => -2,-3  (>(c-1)*b, <=c*b)

ghost int128 div_fu;
function div_fu_cvl(semanticMoneyHarness.FlowRate a,semanticMoneyHarness.Unit b) returns semanticMoneyHarness.FlowRate {
	havoc div_fu assuming ( 
        (a >= 0 &&
        to_mathint(div_fu@new) * to_mathint(b) <= to_mathint(a) &&
        (to_mathint(div_fu@new)+1) * to_mathint(b) > to_mathint(a)) || 
        (a < 0 &&
        to_mathint(div_fu@new) * to_mathint(b) <= to_mathint(a) &&
        (to_mathint(div_fu@new)-1) * to_mathint(b) > to_mathint(a))
	); 
    return div_fu;
}

rule check_mt_t_add_t() {
    uint32 a; uint32 b;
    uint32 c = harness_mt_t_add_t(a, b);
    mathint d = to_mathint(a)+to_mathint(b);
    assert to_mathint(c) == d;
}

rule check_mt_v_sub_v() {
    semanticMoneyHarness.Value a; semanticMoneyHarness.Value b;
    semanticMoneyHarness.Value c = harness_mt_v_sub_v(a, b);
    mathint d = to_mathint(a)-to_mathint(b);
    assert to_mathint(c) == d;
}

rule check_inv_v() {    
    semanticMoneyHarness.Value x;
    semanticMoneyHarness.Value y = harness_inv_v(x);
    mathint z = -1 * to_mathint(x);
    assert to_mathint(y) == z;
}

rule check_mulFU() {    
    semanticMoneyHarness.FlowRate a; semanticMoneyHarness.Unit b;
    semanticMoneyHarness.FlowRate c = harness_mulFU(a, b);
    mathint d = to_mathint(a)*to_mathint(b);
    assert to_mathint(c) == d;
    assert false;
}

rule check_divFU() {    
    semanticMoneyHarness.FlowRate a; semanticMoneyHarness.Unit b;
    semanticMoneyHarness.FlowRate c = harness_divFU(a, b);
    mathint d1 = to_mathint(c)*to_mathint(b);
    mathint d2 = (to_mathint(c)+1)*to_mathint(b);
    mathint d3 = (to_mathint(c)-1)*to_mathint(b);
    assert (c>=0 && to_mathint(a) >= d1 && to_mathint(a) < d2) || 
        (c<0 && to_mathint(a) < d3 && to_mathint(a) >= d1) ;
}

rule check_mulVU() {    
    semanticMoneyHarness.Value a; semanticMoneyHarness.Unit b;
    semanticMoneyHarness.Value c = harness_mulVU(a, b);
    mathint d = to_mathint(a)*to_mathint(b);
    assert to_mathint(c) == d;
}
rule check_mulFT() {    
    semanticMoneyHarness.FlowRate a; semanticMoneyHarness.Time b;
    semanticMoneyHarness.Value c = harness_mulFT(a, b);
    mathint d = to_mathint(a)*to_mathint(b);
    assert to_mathint(c) == d;
} 

rule check_rtbBT() {
    semanticMoneyHarness.BasicParticle a;
    semanticMoneyHarness.Time t;
    semanticMoneyHarness.Value sv = harness_rtbBT(a,t);
    mathint msv = to_mathint(a.flow_rate) * (to_mathint(t)-to_mathint(a.settled_at)) + to_mathint(a.settled_value);
    assert msv == to_mathint(sv);
}

// rule check_pool_member_update() {
//     Time t1; Time t2; Time t3;
//     require t1<t2 && t2<t3;
//     PDPoolMemberMU b1; BasicParticle a; Unit u;
//     harness_pool_member_update(b1, a, u, t1);
// }

    // mt_t_add_t(uint32 a, uint32 b) returns(uint32) => mt_t_add_t_cvl(a, b);

    // mul_nn(semanticMoneyHarness.FlowRate,semanticMoneyHarness.Unit) returns (semanticMoneyHarness.FlowRate) envfree
    // // mul(int128,int128) returns (int128) envfree
    // mul_quotRem(semanticMoneyHarness.FlowRate,semanticMoneyHarness.Unit,semanticMoneyHarness.Unit) returns (semanticMoneyHarness.FlowRate, semanticMoneyHarness.FlowRate) envfree
    // quotRem(semanticMoneyHarness.FlowRate,semanticMoneyHarness.Unit) returns (semanticMoneyHarness.FlowRate,semanticMoneyHarness.FlowRate) envfree
    // // mul_quotRem(int128,uint128,uint128) returns (int128,int128) envfree
    // // rtb(uint32,int256,int128,uint32) returns (int256) envfree
    // // rtb((uint32,int256,int128),uint32) returns (int256) envfree
    // rtbBT(semanticMoneyHarness.BasicParticle,semanticMoneyHarness.Time) returns (semanticMoneyHarness.Value) envfree
// function mt_t_add_t_cvl(uint32 a, uint32 b) returns uint32 {
//    return a + b;
// }

// rule AddVV {
//     semanticMoneyHarness.Value a; semanticMoneyHarness.Value b;
//     semanticMoneyHarness.Value c = add(a, b);
//     mathint d = to_mathint(a)+to_mathint(b);
//     assert to_mathint(c) == d;
// }

// rule MulFU {
//     semanticMoneyHarness.FlowRate a; semanticMoneyHarness.Unit b;
//     semanticMoneyHarness.FlowRate c = mul(a, b);
//     mathint d = to_mathint(a)*to_mathint(b);
//     assert to_mathint(c) == d;
// }

// rule MulFUnn {
//     semanticMoneyHarness.FlowRate a; semanticMoneyHarness.Unit b;
//     semanticMoneyHarness.FlowRate c = mul_nn(a, b);
//     mathint d = to_mathint(a)*to_mathint(b);
//     assert to_mathint(c) == d;
// }

// rule MulFU_np {
//     semanticMoneyHarness.FlowRate a; semanticMoneyHarness.Unit b;
//     require a < 0;
//     require b >= 0;
//     semanticMoneyHarness.FlowRate c = mul(a, b);
//     mathint d = to_mathint(a)*to_mathint(b);
//     assert to_mathint(c) == d;
// }

// rule MulFU_nn {
//     semanticMoneyHarness.FlowRate a; semanticMoneyHarness.Unit b;
//     require a < 0;
//     require b < 0;
//     semanticMoneyHarness.FlowRate c = mul(a, b);
//     mathint d = to_mathint(a)*to_mathint(b);
//     assert to_mathint(c) == d;
// }
// rule MulFU_pp {
//     semanticMoneyHarness.FlowRate a; semanticMoneyHarness.Unit b;
//     require a >= 0;
//     require b >= 0;
//     semanticMoneyHarness.FlowRate c = mul(a, b);
//     mathint d = to_mathint(a)*to_mathint(b);
//     assert to_mathint(c) == d;
// }
// rule MulFU_pn {
//     semanticMoneyHarness.FlowRate a; semanticMoneyHarness.Unit b;
//     require a >= 0;
//     require b < 0;
//     semanticMoneyHarness.FlowRate c = mul(a, b);
//     mathint d = to_mathint(a)*to_mathint(b);
//     assert to_mathint(c) == d;
// }

// rule MulFU_np1 {
//     semanticMoneyHarness.FlowRate a; semanticMoneyHarness.Unit b;
//     require a < 0;
//     require b < 0;
//     semanticMoneyHarness.FlowRate c = mul(a, b);
//     mathint d = to_mathint(a)*to_mathint(b);
//     assert to_mathint(c) == d;
// }

// rule Prove_rtbBT_pp() {
//     semanticMoneyHarness.BasicParticle a;
//     require a.flow_rate >= 0;
//     require a.settled_value >= 0;

//     uint32 t;
//     int256 sv = rtbBT(a,t);
//     mathint psv = to_mathint(a.flow_rate) * (to_mathint(t)-to_mathint(a.settled_at)) + to_mathint(a.settled_value);
//     assert psv == to_mathint(sv);
// }

// rule Prove_rtbBT_pn() {
//     semanticMoneyHarness.BasicParticle a;
//     require a.flow_rate >= 0;
//     require a.settled_value < 0;

//     uint32 t;
//     int256 sv = rtbBT(a,t);
//     mathint psv = to_mathint(a.flow_rate) * (to_mathint(t)-to_mathint(a.settled_at)) + to_mathint(a.settled_value);
//     assert psv == to_mathint(sv);
// }

// rule Prove_rtbBT_np() {
//     semanticMoneyHarness.BasicParticle a;
//     require a.flow_rate < 0;
//     require a.settled_value >= 0;

//     uint32 t;
//     int256 sv = rtbBT(a,t);
//     mathint psv = to_mathint(a.flow_rate) * (to_mathint(t)-to_mathint(a.settled_at)) + to_mathint(a.settled_value);
//     assert psv == to_mathint(sv);
// }

// // https://vaas-stg.certora.com/output/95893/c1c5e3e2e9be4d69a4e1280b420eed8b/?anonymousKey=4cdff42580624e648c2580886127ecc8f65a4713
// rule Prove_rtb_negative() {
//     semanticMoneyHarness.BasicParticle a;
//     require a.flow_rate < 0;
//     require a.settled_value >= 0;
//     uint32 t;
//     int256 sv = rtbBT(a,t);
//     mathint psv = to_mathint(a.flow_rate) * (to_mathint(t)-to_mathint(a.settled_at)) + to_mathint(a.settled_value);
//     assert psv == to_mathint(sv);
// }

// rule Prove_rtbBT_nn() {
//     semanticMoneyHarness.BasicParticle a;
//     uint32 t;
//     require a.flow_rate < 0;
//     require to_mathint(t) - to_mathint(a.settled_value) < 0;

//     int256 sv = rtbBT(a,t);
//     mathint psv = to_mathint(a.flow_rate) * (to_mathint(t)-to_mathint(a.settled_at)) + to_mathint(a.settled_value);
//     assert psv == to_mathint(sv);
// }


// rule MulVU {
//     semanticMoneyHarness.Value a; semanticMoneyHarness.Unit b;
//     semanticMoneyHarness.Value c = mul(a, b);
//     mathint d = to_mathint(a)*to_mathint(b);
//     assert to_mathint(c) == d;
//     assert false;
// }

// rule TimeSub {
//     uint32 a; uint32 b;
//     uint32 c = sub(a, b);
//     mathint d = a-b;
//     assert c == d;
// }

// // rule Revert_FTmul {
// //     int128 r; uint32 t;
// //     int256 c = mul(r, t);
// //     mathint rr = to_mathint(c)/to_mathint(t);
// //     assert t!=0 => to_mathint(r) == rr;
// //     mathint rt = to_mathint(c)/to_mathint(r);
// //     assert r!=0 => to_mathint(t) == rt;
// // }

// rule Revert_FTmul2 {
//     semanticMoneyHarness.FlowRate r; semanticMoneyHarness.Time t;
//     semanticMoneyHarness.Value c = mul(r, t);
//     mathint rr = to_mathint(c)/to_mathint(t);
//     assert t!=0 => to_mathint(r) == rr;
//     mathint rt = to_mathint(c)/to_mathint(r);
//     assert r!=0 => to_mathint(t) == rt;
// }

// rule Revert_FUmul {
//     semanticMoneyHarness.FlowRate r; semanticMoneyHarness.Unit u;
//     semanticMoneyHarness.FlowRate c = mul(r, u);
//     mathint cc = to_mathint(r)*to_mathint(u);
//     assert cc == to_mathint(c);
//     assert false;
//     // mathint rr = to_mathint(c)/to_mathint(u);
//     // assert u!=0 => to_mathint(r) == rr;
//     // mathint ru = to_mathint(c)/to_mathint(r);
//     // assert r!=0 => to_mathint(u) == ru;
// }
// // c -15
// // r 15
// // rr -1
// // u MAX_UINT128 (0xffffffffffffffffffffffffffffffff)

// rule Revert_quotRem {
//     semanticMoneyHarness.FlowRate r; semanticMoneyHarness.Unit u;
//     semanticMoneyHarness.FlowRate nr; semanticMoneyHarness.FlowRate er;
//     nr, er = quotRem(r, u);
//     mathint rr = (to_mathint(nr) * to_mathint(u) + to_mathint(er));
//     assert u!=0 => rr == to_mathint(r); 
// }

// rule Revert_mul_quotRem {
//     semanticMoneyHarness.FlowRate r; semanticMoneyHarness.Unit u1; semanticMoneyHarness.Unit u2;
//     semanticMoneyHarness.FlowRate nr; semanticMoneyHarness.FlowRate er;
//     nr, er = mul_quotRem(r, u1, u2);
//     mathint rr = (to_mathint(nr) * to_mathint(u2) + to_mathint(er)) / to_mathint(u1);
//     assert u1!=0 => rr == to_mathint(r); 
// }

// // r  15
// // u1  2
// // u2 0xfffffffffffffffffffffffffffffff9
// // nr -4
// // er 30
// // rr -0x1ffffffffffffffffffffffffffffffe3

// // int128(0xfffffffffffffffffffffffffffffff9) == -7


// // rule Prove_rtb() {
// //     uint32 a_t; int256 a_v; int128 a_f;
// //     uint32 t;
// //     int256 sv = rtb(a_t,a_v,a_f,t);
// //     mathint psv = to_mathint(a_f) * (to_mathint(t)-to_mathint(a_t)) + to_mathint(a_v);
// //     assert psv == to_mathint(sv);
// // }

// rule Prove_rtbBT_positive() {
//     semanticMoneyHarness.BasicParticle a;
//     require a.flow_rate >= 0;
//     // require a.settled_value >= 0;
//     semanticMoneyHarness.Time t;
//     semanticMoneyHarness.Value sv = rtbBT(a,t);
//     mathint psv = to_mathint(a.flow_rate) * (to_mathint(t)-to_mathint(a.settled_at)) + to_mathint(a.settled_value);
//     assert psv == to_mathint(sv);
// }

// rule Prove_rtbBT_negative() {
//     semanticMoneyHarness.BasicParticle a;
//     require a.flow_rate < 0;
//     require a.settled_value > 0;
//     semanticMoneyHarness.Time t;
//     semanticMoneyHarness.Value sv = rtbBT(a,t);
//     mathint psv = to_mathint(a.flow_rate) * (to_mathint(t)-to_mathint(a.settled_at)) + to_mathint(a.settled_value);
//     assert psv == to_mathint(sv);
// }



