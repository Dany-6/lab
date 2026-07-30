# Threat Intelligence Collection using OSINT
# Kali Linux
import subprocess
print(&quot;=======================================&quot;)
print(&quot; OSINT Threat Intelligence Collection&quot;)
print(&quot;=======================================\n&quot;)
domain = input(&quot;Enter Target Domain: &quot;)
print(&quot;\n========== WHOIS Information ==========\n&quot;)
try:
subprocess.run([&quot;whois&quot;, domain])
except:
print(&quot;WHOIS command not found.&quot;)
print(&quot;\n========== DNS Information ==========\n&quot;)
try:
subprocess.run([&quot;dig&quot;, domain])
except:
print(&quot;DIG command not found.&quot;)
print(&quot;\nThreat Intelligence Collection Completed.&quot;)
