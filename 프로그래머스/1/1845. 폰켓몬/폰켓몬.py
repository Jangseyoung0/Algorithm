def solution(nums):
    pocketmon=list(set(nums))
    if len(pocketmon)>len(nums)//2:
        answer = len(nums)//2
    else:
        answer = len(pocketmon)
    return answer