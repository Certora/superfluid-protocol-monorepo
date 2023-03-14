// using SemanticMoneyHarness as semanticMoneyHarness

methods {
    // distriutor() returns (address) => DISPATCHER(true)
    // getIndex() returns ((uint128,(uint32,int256,int128))) => DISPATCHER(true)
    // setIndex(semanticMoneyHarness.PDPoolIndex) => DISPATCHER(true)
    // // getMember(address) returns ((semanticMoneyHarness.Unit,semanticMoneyHarness.Value,semanticMoneyHarness.BasicParticle)) => DISPATCHER(true)
    // getMember(address) returns ((int128,int256,(uint32,int256,int128))) => DISPATCHER(true)
    // updatePoolMember(address, semanticMoneyHarness.Unit) returns (bool) => DISPATCHER(true)
    // getIndex() returns ((uint128,(uint32,int256,int128))) envfree
    // setIndex((uint128,(uint32,int256,int128))) envfree
    // getMember(address) returns ((uint128,int256,())) envfree
    // updatePoolMember(address, uint128,(uint32,int256,int128)) returns (bool) envfree

    transferFrom(address from, address to, uint256 amount) returns (bool) envfree
    uIndexes(address) returns (uint32,int256,int128) envfree
}

// https://vaas-stg.certora.com/output/95893/7f60cf85a8584225a4c0e40b9a071763?anonymousKey=8e35083adba38d891aa7f412141531476f948ea2
rule check_transfer() {
    address from; address to; uint256 amount;
    int256 _from_settled_value;
    int256 _to_settled_value;
    _,_from_settled_value,_ = uIndexes(from);
    _,_to_settled_value,_ = uIndexes(to);

    bool successful = transferFrom(from, to, amount);

    int256 from_settled_value_;
    int256 to_settled_value_;
    _,from_settled_value_,_ = uIndexes(from);
    _,to_settled_value_,_ = uIndexes(to);

    assert to_mathint(_from_settled_value) - to_mathint(amount) == to_mathint(from_settled_value_);
    assert to_mathint(_to_settled_value) + to_mathint(amount) == to_mathint(to_settled_value_);
}

// ghost ghostSupply() returns uint256;
// // the hook that updates the ghost function as follows
// // "At every write to the value at key 'a' in 'balances'
// // increase ghostTotalSupply by the difference between
// // tho old value and the new value"
// //                              the new value ↓ written:
// hook Sstore balances[KEY address a] uint256 balance
// // the old value ↓ already there
//     (uint256 old_balance) STORAGE {
//   havoc ghostSupply assuming ghostSupply@new() == ghostSupply@old() +
//       (balance - old_balance);
// }
 
// hook Sstore balanceOf[KEY uint a] uint balance (uint oldBalance) STORAGE {
//     havoc shareSum assuming shareSum@new == shareSum@old + balance - oldBalance;
// }
 

// ghost mapping(uint256 => mathint) sumOfBalances {
//     init_state axiom forall uint256 token . sumOfBalances[token] == 0;
// }

// hook Sstore _balances[KEY uint256 token][KEY address user] uint256 newValue (uint256 oldValue) STORAGE {
//     sumOfBalances[token] = sumOfBalances[token] + newValue - oldValue;
// }

// /// The sum of the balances over all users must equal the total supply for a 
// /// given token.
// invariant total_supply_is_sum_of_balances(uint256 token)
//     sumOfBalances[token] == totalSupply(token)
//     {
//         preserved {
//             requireInvariant balanceOfZeroAddressIsZero(token);
//         }
//     }

// ghost mapping(address => mathint) balances;

// hook Sstore balances[KEY address a] uint256 balance
// // the old value ↓ already there
//     (uint256 old_balance) STORAGE {
//   havoc ghostSupply assuming ghostSupply@new() == ghostSupply@old() +
//       (balance - old_balance);
// }

// /// The balance of a token for the zero address must be zero.
// invariant balanceOfZeroAddressIsZero()
//     balanceOf(0) == 0 