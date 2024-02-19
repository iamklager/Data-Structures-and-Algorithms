# Chapter 07

## Exercise 05

I once saw a joke aimed at HR people: "Want to immediately eliminate the unluckiest people from your hiring process? Just take half of the resumes on your desk and throw them in the trash."

If we were to write software that kept reducing a pile of resumes until we had one left, it might take the approach of alternating between throwing out the top half and the bottom half. That is, it will first eliminate the top half of the pile, and then proceed to eliminate the bottom  half of what remains. It keeps alternating between eliminating the top and bottom until one lucky resume remains, and that's who we'll hire!

Describe the efficiency of this function in terms of Big O:

```ruby
def pick_resume(resumes)
  eliminate = "top"
  
  while resumes.length > 1
    if eliminate == "top"
      resumes = resumes[resumes.length / 2, resumes.length - 1]
      eliminate = "bottom"
    elsif eliminate == "bottom"
      resumes = resumes[0, resumes.length / 2]
      eliminate = "top"
    end
  end
  
  return resumes[0]
end
```

$O(\log N)$
