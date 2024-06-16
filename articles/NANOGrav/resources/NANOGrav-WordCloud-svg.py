from wordcloud import WordCloud

# Dosyanızın yolu
text_file_path = 'F:\\OneDrive - Centaurioun\\ScientificRadar\\articles\\NANOGrav\\NANOGrav.md'
svg_file_path = 'F:\\OneDrive - Centaurioun\\ScientificRadar\\articles\\NANOGrav\\NANOGrav_wordcloud.svg'

# Metni dosyadan oku
with open(text_file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Word Cloud oluştur
wordcloud = WordCloud(background_color='white').generate(text)

# Word Cloud'u SVG dosyası olarak kaydet
with open(svg_file_path, 'w', encoding='utf-8') as f:
    f.write(wordcloud.to_svg())

# Eğer Word Cloud'u göstermek istiyorsanız, gösterim için PNG formatında bir dosya da oluşturabilirsiniz.
# PNG dosyasının yolu
png_file_path = 'F:\\OneDrive - Centaurioun\\ScientificRadar\\articles\\NANOGrav\\NANOGrav_wordcloud.png'

# Word Cloud'u PNG dosyası olarak kaydet
wordcloud.to_file(png_file_path)
