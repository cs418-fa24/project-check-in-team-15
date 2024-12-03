def compare_tweets(before_file, after_file, positive_words, negative_words):
    before_tone, before_word_freq = analyze_tweets(before_file, positive_words, negative_words)
    after_tone, after_word_freq = analyze_tweets(after_file, positive_words, negative_words)
    
    tone_categories = ["Positive", "Negative", "Neutral"]
    before_counts = [before_tone.get(tone, 0) for tone in tone_categories]
    after_counts = [after_tone.get(tone, 0) for tone in tone_categories]

    fig, ax = plt.subplots(figsize=(10, 6))
    bar_width = 0.5
    
    index = range(len(tone_categories))
    ax.bar(index, before_counts, bar_width, label='Before Election', color='skyblue')
    ax.bar(index, after_counts, bar_width, bottom=before_counts, label='After Election', color='salmon')
    
    ax.set_xlabel('Tone Categories')
    ax.set_ylabel('Frequency')
    ax.set_title('Stacked Tone Comparison Before and After Election')
    ax.set_xticks(index)
    ax.set_xticklabels(tone_categories)
    ax.legend()

    plt.tight_layout()
    plt.show()
