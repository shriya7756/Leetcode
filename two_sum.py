def two_sum(nums, target):
    dic = {}  # Create an empty dictionary
    for i in range(len(nums)):  # Iterate through the list
        rem = target - nums[i]  # Calculate the required complement
        if rem in dic:  # Check if complement exists in dictionary
            return [dic[rem], i]  # Return indices of the two numbers
            
        else:
            dic[nums[i]] = i  # Store the current number's index in dictionary
            print(dic)
    return []
nums=[22,3,4,5,6]
print(two_sum(nums, 9))
