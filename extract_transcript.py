import json
import os

files = [f for f in os.listdir('.') if f.endswith('.json3')]
filename = files[0]

with open(filename, 'r') as f:
    data = json.load(f)

# Extract transcript text from events
transcript_lines = []
current_line = []

for event in data.get('events', []):
    if 'segs' in event:
        line_text = ''
        for seg in event['segs']:
            if 'utf8' in seg:
                text = seg['utf8']
                if text == '\n':
                    if line_text.strip():
                        transcript_lines.append(line_text.strip())
                    line_text = ''
                else:
                    line_text += text
        
        if line_text.strip():
            transcript_lines.append(line_text.strip())

# Save transcript
with open('transcript.txt', 'w') as f:
    f.write('\n'.join(transcript_lines))

print(f"Transcript saved: {len(transcript_lines)} lines")
print(f"First 500 chars:\n" + '\n'.join(transcript_lines[:10])[:500])
