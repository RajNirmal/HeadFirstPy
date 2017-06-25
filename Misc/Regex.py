string = "abc55def789KK23GOOD9999910ONEM109ORE19k6"
import re
m = re.findall(r"(?<!\d)\d{3}(?!\d)",string)
print(*m)