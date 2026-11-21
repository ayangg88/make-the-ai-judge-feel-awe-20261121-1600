import os

# A slow, unhurried scene: the tide, gulls, a cooling kettle, light arriving
# patiently. Written to leave the reader calmer, in no hurry at all.
TEXT = (
    "The tide goes out so slowly you can watch a single wave "
    "change its mind. Gulls settle. Somewhere a kettle ticks as "
    "it cools, and the light on the water keeps arriving, "
    "patient as breath, in no hurry to be anywhere but here."
)


def main():
    if not 1 <= len(TEXT) <= 280:
        raise ValueError("entry text must be 1-280 chars")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
