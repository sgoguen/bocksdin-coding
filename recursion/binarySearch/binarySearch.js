const binarySearch = (sortedArr, startIdx = 0, endIdx = sortedArr.length - 1, target) => {
  const midIdx = Math.floor((endIdx - startIdx) / 2) + startIdx;
  console.log(sortedArr, startIdx, endIdx, target);

  if (sortedArr[midIdx] === target) return `Target (${target}) located at index (${midIdx})`;

  if (target < sortedArr[midIdx]) return binarySearch(sortedArr, startIdx, midIdx, target);
  else return binarySearch(sortedArr, midIdx + 1, endIdx, target);
}

// binarySearch([1, 2, 3, 4, 5], 0, 4, 5);
//  -> binarySearch([1, 2, 3, 4, 5], 3, 4, 5);
//    -> binarySearch([1, 2, 3, 4, 5], 4, 4, 5) -> Target (5) is located at index (4)







