# Chapter 07

## Exercise 03

Use Big O Notation to describe the time complexity of the following function. This function solves a famous problem known as "finding a needle in the haystack."

Both the needle and haystack are strings. For example, if the needle is "def" and the haystack is "abcdefghi", the needle is contained somewhere in the haystack, as "def" is a substring of "abcdefghi". However, if the needle is "dd", it cannot be found in the haystack of "abcdefghi".

This function returns true or false, depending on whether the needle can be found in the haystack:
```ruby
def find_needle(needle, haystack)
  needle_start_index = 0
  
  while needle_start_index <= haystack.length - needle.length
    if needle[0] == haystack[needle_start_index]
      needle_offset = 0
      
      while needle_offset < needle.length
        if needle[needle_offset] != haystack[needle_start_index + needle_offset]
          break
        else
          if needle_offset == needle.length - 1
            return true
          end
        end
        needle_offset += 1
      end
    end
    
    needle_start_index += 1
  end
  
  return false
end
```

$O(N \cdot M)$
