pragma solidity 0.8.19;

import "../../src/SemanticMoney.sol";

contract SemanticMoneyHarness {
    // // AdditionalMonetaryTypeHelpers
    function harness_mt_t_add_t(Time a, Time b) public returns (Time) {
        return mt_t_add_t(a,b);
    }    
    
    function harness_mt_v_sub_v(Value a, Value b) public returns (Value) {
        return mt_v_sub_v(a,b);
    }
    function harness_inv_v(Value x) public returns (Value) {
        return AdditionalMonetaryTypeHelpers.inv(x);
    }
    function harness_mulFU(FlowRate r, Unit u) public returns (FlowRate) {
        return AdditionalMonetaryTypeHelpers.mul(r, u);
    } 
    function harness_divFU(FlowRate r, Unit u) public returns (FlowRate) {
        return AdditionalMonetaryTypeHelpers.div(r, u);
    }
    function harness_mulVU(Value a, Unit b) public returns (Value) {
        return AdditionalMonetaryTypeHelpers.mul(a, b);
    }
    function harness_mulFT(FlowRate r, Time t) public returns (Value) {
        return AdditionalMonetaryTypeHelpers.mul(r, t);
    }
    function harness_rtbBT(BasicParticle memory a, Time t) public returns (Value v) {
        return SemanticMoney.rtb(a, t);  
    }

    function harness_clonePI(PDPoolIndex memory a) public
        returns (PDPoolIndex memory b) {
        return SemanticMoney.clone(a);    
    }
    function harness_pool_member_update(PDPoolMemberMU memory b1, BasicParticle memory a, Unit u, Time t) public
        returns (PDPoolIndex memory p, PDPoolMember memory p1, BasicParticle memory b) {
        return SemanticMoney.pool_member_update(b1, a, u, t);
    }
    // function sub(Time a, Time b) public returns (Time) {
    //     return mt_t_sub_t(a, b);
    // }

    // ////////////////////////////////////////////////////////////
    // // Value
    // ////////////////////////////////////////////////////////////
    // function inv(Value x) public returns (Value) {
    //     return AdditionalMonetaryTypeHelpers.inv(x);
    // }
    // function add(Value a, Value b) public returns (Value) {
    //     return mt_v_add_v(a, b);
    // }
    // function sub(Value a, Value b) public returns (Value) {
    //     return mt_v_sub_v(a,b);
    // }
    // function mul(Value a, Unit b) public returns (Value) {
    //     return AdditionalMonetaryTypeHelpers.mul(a,b);
    // }

    // function div(Value a, Unit b) public returns (Value) {
    //     return AdditionalMonetaryTypeHelpers.div(a,b);
    // }

    // ////////////////////////////////////////////////////////////
    // // Unit
    // ////////////////////////////////////////////////////////////

    // function addUU(Unit a, Unit b) public returns (Unit) {
    //     return mt_u_add_u(a, b);
    // }
    // function subUU(Unit a, Unit b) public returns (Unit) {
    //     return mt_u_sub_u(a, b);
    // }

    // ////////////////////////////////////////////////////////////
    // // FlowRate
    // ////////////////////////////////////////////////////////////
    // function addFF(FlowRate a, FlowRate b) public returns (FlowRate) {
    //     return AdditionalMonetaryTypeHelpers.add(a,b);
    // }
    // function subFF(FlowRate a, FlowRate b) public returns (FlowRate) {
    //     return AdditionalMonetaryTypeHelpers.sub(a, b);
    // }
    // function inv(FlowRate r) public returns (FlowRate) {
    //     return AdditionalMonetaryTypeHelpers.inv(r);
    // }

    // ////////////////////////////////////////////////////////////
    // // FlowRate & Time
    // ////////////////////////////////////////////////////////////
    // function mul(FlowRate r, Time t) public returns (Value) {
    //     return AdditionalMonetaryTypeHelpers.mul(r, t);
    // }

    // ////////////////////////////////////////////////////////////
    // // FlowRate & Unit
    // ////////////////////////////////////////////////////////////
    // function mul(FlowRate r, Unit u) public returns (FlowRate) {
    //     return AdditionalMonetaryTypeHelpers.mul(r, u);
    // }

    // // function mul_nn(FlowRate f, Unit u) public returns (FlowRate) {
    // //     return AdditionalMonetaryTypeHelpers.mul_nn(f, u);
    // // }

    // function div(FlowRate a, Unit b) public returns (FlowRate) {
    //     return AdditionalMonetaryTypeHelpers.div(a, b);
    // }
    // function quotRem(FlowRate r, Unit u) public returns (FlowRate nr, FlowRate er) {
    //     return AdditionalMonetaryTypeHelpers.quotRem(r, u);
    // }

    // function mul_quotRem(FlowRate r, Unit u1, Unit u2) public returns (FlowRate nr, FlowRate er) {
    //     return AdditionalMonetaryTypeHelpers.mul_quotRem(r, u1, u2);
    // }

    // // SemanticMoney
    // function clone(BasicParticle memory a) public returns (BasicParticle memory b) {
    //     return SemanticMoney.clone(a);
    // }

    // function settle(BasicParticle memory a, Time t) public returns (BasicParticle memory b) {
    //     return SemanticMoney.settle(a, t);
    // }

    // // function rtb(uint32 a_t, int256 a_v, int128 a_f, Time t) public returns (Value v) {
    // //     BasicParticle memory a;
    // //     a.flow_rate = FlowRate.wrap(a_f);
    // //     a.settled_at = Time.wrap(a_t);
    // //     a.settled_value = Value.wrap(a_v);
    // //     return SemanticMoney.rtb(a, t);
    // // }

    // // function rtb(uint32 a_t, int256 a_v, int128 a_f, Time t) public returns (Value v) {
    // //     return SemanticMoney.rtb(a_t, a_v, a_f, t);
    // // }

    // function rtbBT(BasicParticle calldata a, Time t) public returns (Value v) {
    //     return SemanticMoney.rtb(a, t);
    // }


    // function shift1(BasicParticle memory a, Value x) public returns (BasicParticle memory b) {
    //     return SemanticMoney.shift1(a, x);
    // }

    // function flow1(BasicParticle memory a, FlowRate r) public returns (BasicParticle memory b) {
    //     return SemanticMoney.flow1(a, r);
    // }

    // //
    // // Universal Index to Universal Index 2-primitives
    // //


    // function mappend(BasicParticle memory a, BasicParticle memory b)
    //     public returns (BasicParticle memory c) {
    //         return SemanticMoney.mappend(a, b);
    // }

    // function shift2(BasicParticle memory a, BasicParticle memory b, Value x) public 
    //     returns (BasicParticle memory m, BasicParticle memory n) {
    //     return SemanticMoney.shift2(a, b, x);
    // }

    // function flow2(BasicParticle memory a, BasicParticle memory b, FlowRate r, Time t) public 
    //     returns (BasicParticle memory m, BasicParticle memory n) {
    //     return SemanticMoney.flow2(a, b, r, t);
    // }

    // //
    // // Pool operations
    // //
    // // updp_: universal index to proportional distribution pool
    // //

    // function clone(PDPoolIndex memory a) public returns (PDPoolIndex memory b) {
    //     return SemanticMoney.clone(a);
    // }

    // function settle(PDPoolIndex memory a, Time t) public 
    //     returns (PDPoolIndex memory m)
    // {
    //     return SemanticMoney.settle(a, t);
    // }

    // function shift2(BasicParticle memory a, PDPoolIndex memory b, Value x) public 
    //     returns (BasicParticle memory m, PDPoolIndex memory n, Value x1) {
    //     return SemanticMoney.shift2(a, b, x);
    // }

    // function flow2(BasicParticle memory a, PDPoolIndex memory b, FlowRate r, Time t) public 
    //     returns (BasicParticle memory m, PDPoolIndex memory n, FlowRate r1)
    // {
    //     return SemanticMoney.flow2(a, b, r, t);
    // }


    // function clone(PDPoolMember memory a) public returns (PDPoolMember memory b) {
    //     return SemanticMoney.clone(a);
    // }

    // function settle(PDPoolMemberMU memory a, Time t) public 
    //     returns (PDPoolMemberMU memory b)
    // {
    //     return SemanticMoney.settle(a, t);
    // }

    // function rtbPT(PDPoolMemberMU memory a, Time t) public 
    //     returns (Value v)
    // {
    //     return SemanticMoney.rtb(a, t);
    // }

    // // Update the unit amount of the member of the pool
    // function pool_member_update(PDPoolMemberMU memory b1, BasicParticle memory a, Unit u, Time t)
    //     public 
    //     returns (PDPoolIndex memory p, PDPoolMember memory p1, BasicParticle memory b)
    // {
    //     return SemanticMoney.pool_member_update(b1, a, u, t);
    // }
}