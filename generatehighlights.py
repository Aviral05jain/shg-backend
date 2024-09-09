from Eventdetect import detect_audio_events,detect_visual_events,analyze_commentary
def generate_highlights_feed(combined_events, video_duration):
    highlights = []
    event_start = None
    
    for i in range(len(combined_events)):
        if combined_events[i] and event_start is None:
            event_start = i
        elif not combined_events[i] and event_start is not None:
            event_end = i
            highlights.append((event_start, event_end))
            event_start = None
    
    # Return highlights with timestamps
    return [(start, end) for start, end in highlights]
