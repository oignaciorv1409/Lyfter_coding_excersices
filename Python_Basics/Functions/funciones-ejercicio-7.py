# “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”

text = "python-variable-funcion-computadora-monitor"
words = text.split("-")

def to_sort_string (words):
        words.sort()
        
        return "-".join(words)

sorted_words = to_sort_string (words)
print (sorted_words)