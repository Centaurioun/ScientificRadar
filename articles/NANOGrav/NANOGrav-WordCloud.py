from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Read your text from the file
text = open('F:\\OneDrive - Centaurioun\\ScientificRadar\\articles\\NANOGrav\\NANOGrav.md', encoding='utf-8').read()

# Create a word cloud with high resolution
wordcloud = WordCloud(width=2000, height=1000, background_color='white').generate(text)

# Save the image in the img folder:
wordcloud.to_file('F:\\OneDrive - Centaurioun\\ScientificRadar\\articles\\NANOGrav\\NANOGrav_high_res.png')

# Display the generated Word Cloud
plt.figure(figsize=(20, 10), dpi=300)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
