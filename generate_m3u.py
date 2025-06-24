import json

with open("toffee_channel_data.json", "r", encoding="utf-8") as f:
    channels = json.load(f)

with open("toffee_playlist.m3u", "w", encoding="utf-8") as out:
    out.write("#EXTM3U\n")
    
    for ch in channels:
        if isinstance(ch, dict):
            name = ch.get("display_name") or ch.get("name") or "No Name"
            logo = ch.get("logo") or ""
            url = ch.get("url") or ch.get("stream_url") or ""
            
            if not url:
                continue
            
            out.write(f'#EXTINF:-1 tvg-logo="{logo}",{name}\n{url}\n')
        else:
            # যদি ch string হয়, ধরে নাও এটা শুধু url
            out.write(f'#EXTINF:-1,{ch}\n{ch}\n')
