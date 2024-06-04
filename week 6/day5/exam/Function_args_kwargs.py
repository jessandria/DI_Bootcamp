def combine_words(*args, **kwargs):
    
    positional_part = ' '.join(args)
    
    
    sorted_keywords = sorted(kwargs.items())
    keyword_part = ' '.join(value for key, value in sorted_keywords)
    
    
    combined_sentence = f"{positional_part}. {keyword_part}"
    
    return combined_sentence


print(combine_words("Hello", "world", second="is", third="great!", first="Python"))

