import os
import re

def standardize_quotes(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern for Vol 1 Quote
    # <div class="py-10 md:py-16 my-8 md:my-12 relative bg-surface-container-lowest/50 border-y border-outline-variant/20 flex justify-center w-[100vw] left-1/2 right-1/2 -ml-[50vw] -mr-[50vw]">
    # <div class="px-6 md:px-8 text-center relative max-w-4xl mx-auto flex items-center justify-center">
    #     <span class="material-symbols-outlined text-primary/10 absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 text-[8rem] md:text-[12rem] leading-none pointer-events-none -z-10">format_quote</span>
    #     <blockquote class="font-headline text-xl sm:text-2xl md:text-3xl lg:text-4xl italic text-primary leading-loose md:leading-loose tracking-widest relative z-10">
    #         别再等待，去创造你的“作品”。<br>不需要完美，只需要真诚。
    #     </blockquote>
    # </div>
    # </div>
    
    # We will just replace everything that looks like the old blockquote structure with the new standardized one
    # that uses leading-[2.5] and natural wrapping (no <br class="md:hidden"/>).

    # First, let's remove any <br class="md:hidden"/> from the quotes
    content = content.replace('<br class="md:hidden"/>', '')

    # Replace leading-loose md:leading-loose with leading-[2.5] in blockquotes
    content = re.sub(r'(<blockquote[^>]*class="[^"]*)leading-loose md:leading-loose([^"]*")', r'\1leading-[2.5]\2', content)

    # Vol 1 specific fix: the quote was changed to:
    # <blockquote class="font-headline text-fluid-xl italic text-primary leading-[2.5] tracking-widest relative z-10">
    #     别再等待，去创造你的“作品”。<br>不需要完美，只需要真诚。
    # </blockquote>
    # Let's just make sure it's leading-[2.5] and tracking-widest and break-keep
    content = re.sub(
        r'<blockquote class="font-headline text-fluid-xl italic text-primary leading-\[2\.5\] tracking-widest relative z-10">',
        r'<blockquote class="font-headline text-2xl sm:text-3xl md:text-4xl italic text-primary leading-[2.5] tracking-widest break-keep relative z-10">',
        content
    )
    
    # Vol 2 specific fix:
    # <blockquote class="font-headline text-2xl sm:text-3xl md:text-4xl italic text-[#B44C2E] leading-[2.5] tracking-widest relative z-10">
    # “建立信任始于规避风险，成于专业可靠，最终才导向价值交换。”
    content = re.sub(
        r'<blockquote class="font-headline text-2xl sm:text-3xl md:text-4xl italic text-\[#B44C2E\] leading-\[2\.5\] tracking-widest relative z-10">',
        r'<blockquote class="font-headline text-2xl sm:text-3xl md:text-4xl italic text-[#B44C2E] leading-[2.5] tracking-widest break-keep relative z-10">',
        content
    )

    # Vol 3 specific fix:
    # <blockquote class="font-headline text-2xl sm:text-3xl md:text-4xl italic text-primary leading-[2.5] tracking-widest relative z-10">
    # “忠于自我，就是最好的人生脚本。”
    content = re.sub(
        r'<blockquote class="font-headline text-2xl sm:text-3xl md:text-4xl italic text-primary leading-\[2\.5\] tracking-widest relative z-10">',
        r'<blockquote class="font-headline text-2xl sm:text-3xl md:text-4xl italic text-primary leading-[2.5] tracking-widest break-keep relative z-10">',
        content
    )
    
    # Vol 4 specific fix (if any):
    content = re.sub(
        r'<blockquote class="font-headline text-2xl sm:text-3xl md:text-4xl italic text-primary leading-\[2\.5\] tracking-widest relative z-10">',
        r'<blockquote class="font-headline text-2xl sm:text-3xl md:text-4xl italic text-primary leading-[2.5] tracking-widest break-keep relative z-10">',
        content
    )

    # Make sure all quote backgrounds have the flex items-center justify-center and absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2
    # This was mostly handled in the previous script, but let's ensure it's exact.
    # The previous script did this:
    # <span class="material-symbols-outlined text-[#B44C2E]/10 absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 text-[8rem] md:text-[16rem] leading-none pointer-events-none -z-10">format_quote</span>

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for root, dirs, files in os.walk('episodes'):
    for file in files:
        if file.endswith('.html'):
            standardize_quotes(os.path.join(root, file))

print("Standardized all quotes to design system V3.")
