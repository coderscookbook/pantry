// find the indecies of two items in array that add up to the target value
// return the indecies in an array
const nums = [2, 7, 11, 15]
const target = 22

function solution(nums, target) {
  let map = new Map()
  
  for(let i = 0; i<nums.length; i++){
    // get the compliment
    let compliment = target - nums[i];
    if(map.has(compliment)){
      return [i, map.get(compliment)];
    } else {
      map.set(nums[i], i)
    }
  }
}

// let solutions = solution(nums, target)
console.log(solution(nums, target)) // returns [3, 1]