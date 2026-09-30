def isHappy(n):
    isthere=[False for i in range(811)]
    temp=0
    while isthere[temp]==False and n>1:
        isthere[temp]=True
        temp=0
        while n>0:
            temp+=(n%10)*(n%10)
            n//=10
        n=temp
    return n==1


if __name__ == "__main__":
    sample0_output = isHappy(19)
    sample1_output = isHappy(2)
    with open("/app/bind_mount/output.txt", "w") as f:
        f.write(f"19: {sample0_output}\n")
        f.write(f"2: {sample1_output}\n")
    print("Results saved to /app/bind_mount/output.txt")