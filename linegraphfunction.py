def compare_tweets(before_file, after_file, positive_words, negative_words):
    before_tone, before_word_freq = analyze_tweets(before_file, positive_words, negative_words)
    after_tone, after_word_freq = analyze_tweets(after_file, positive_words, negative_words)

    tone_categories = ["Positive", "Negative", "Neutral"]
    before_counts = [before_tone.get(tone, 0) for tone in tone_categories]
    after_counts = [after_tone.get(tone, 0) for tone in tone_categories]

    x = ['Before Election', 'After Election']

    fig, ax = plt.subplots(figsize=(10, 6))
    for i, tone in enumerate(tone_categories):
        ax.plot(x, [before_counts[i], after_counts[i]], marker='o', label=tone)

    ax.set_xlabel('Election Period')
    ax.set_ylabel('Frequency')
    ax.set_title('Tone Comparison Before and After Election')
    ax.legend(title="Tone Categories")

    plt.tight_layout()
    plt.show()