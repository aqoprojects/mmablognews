from  django.db import migrations
from django.contrib.contenttypes.models import ContentType
from mmablog.models import BlogPost, BlogCategory
from django.contrib.auth import get_user_model

def BlogEntries(apps, scheme_eiditor):
    Blogpost = apps.get_model("mmablog.BlogPost")
    content_type = ContentType.objects.get_for_model(BlogPost)

    # Sample users for author and publisher
    author, created =  get_user_model().objects.get_or_create(username="user", email='user')
    if created:
        author.set_password("user")
        author.is_superuser = True
        author.is_active = True
        author.save()
    publisher = author

    # Category instances
    wwe, created = BlogCategory.objects.get_or_create(name="wwe")
    tna, created = BlogCategory.objects.get_or_create(name="tna")
    aew, created = BlogCategory.objects.get_or_create(name="aew")
    # football = BlogCategory.objects.get(name="football")
    njpw, created = BlogCategory.objects.get_or_create(name="njpw")

    blogs = [
        {
            "topic": "Oba Femi: NXT's Next Powerhouse",
            "article": """Oba Femi, the Nigerian-born sensation, has taken WWE NXT by storm. His remarkable blend of size, agility, and in-ring psychology makes him one of the most exciting prospects in professional wrestling today. Since debuting, Femi has dominated competition with a blend of brute force and surprising agility. His powerful persona has reminded fans of legendary big men like Batista and Bobby Lashley, but with a modern flair. His recent matches have showcased not only his physical prowess but also his ability to tell a story in the ring. Many fans and analysts believe he’s on a fast track to the main roster and could be a WrestleMania main-eventer in the next few years.""",
            "category": wwe
        },
        {
            "topic": "Moose and the TNA Resurgence",
            "article": """Moose has become a cornerstone of TNA’s renaissance. The former NFL lineman has transitioned seamlessly into wrestling, combining legitimate athleticism with a commanding ring presence. His character development over the last few years has seen him evolve from a brash upstart into a dominant world champion. Moose’s recent title defenses have been some of the most talked-about moments in TNA, proving that the company still has the potential to deliver main-event-level performances. As the face of TNA, Moose continues to elevate younger talent while also asserting his dominance at the top of the card.""",
            "category": tna
        },
        {
            "topic": "Rhea Ripley: The Nightmare Returns",
            "article": """Rhea Ripley has carved out a unique legacy in WWE. With her punk rock aesthetic, no-nonsense demeanor, and unmatched intensity, she stands as one of the most formidable women in professional wrestling. Her matches are brutal, emotionally charged, and technically sound. After a brief hiatus, her return sent shockwaves through the women’s division. Her feud with Liv Morgan is setting the standard for storytelling and brutality in women’s wrestling today. Ripley’s work ethic and connection with the audience have cemented her status as a generational talent.""",
            "category": wwe
        },
        {
            "topic": "Alexa Bliss: Beyond the Twisted Persona",
            "article": """Alexa Bliss has consistently reinvented herself throughout her WWE career. From the sparkly, entitled heel to the darker, more twisted character associated with Bray Wyatt, she has shown remarkable range. While she has taken a brief hiatus recently, her legacy is undeniable. Multiple title reigns, standout promos, and iconic matches against top-tier opponents have defined her journey. Fans eagerly await her return, with speculation running rampant about what version of Bliss will step through the curtain next. One thing is certain: she will captivate audiences once again.""",
            "category": wwe
        },
        {
            "topic": "Charlotte Flair: The Queen's Legacy",
            "article": """Charlotte Flair is arguably the most decorated female wrestler in WWE history. With a championship pedigree and athleticism that rivals anyone on the roster, she has consistently delivered main event-caliber performances. Her matches with Sasha Banks, Becky Lynch, and Ronda Rousey are still talked about as some of the best in women's wrestling. Despite criticism about frequent title reigns, her consistency and dedication to her craft are undisputed. Charlotte’s influence on the current women’s division is immense, and her legacy is already firmly etched into WWE’s history books.""",
            "category": wwe
        },
        # Repeat similar blocks with variations for a total of 16 blogs
    ]

    # Duplicate and vary articles slightly for more entries
    import random
    import lorem

    for i in range(6, 17):
        star = random.choice(["Oba Femi", "Moose", "Rhea Ripley", "Alexa Bliss", "Charlotte Flair"])
        cat = random.choice([wwe, tna, aew, njpw])
        topic = f"{star} and the Future of Wrestling in 2025"
        article = f"""This is a deep dive into {star}'s impact on the industry. {lorem.paragraph()} {lorem.paragraph()} {lorem.paragraph()}"""
        
        blog_create = BlogPost.objects.create(
            topic=topic,
            article=article,
            category=cat,
            publisher=publisher
        )
        blog_create.author.add(author)

    

class Migration(migrations.Migration):

    dependencies = [
    #   ("0001_initial", "0002_auto_files")
    ('mmablog', '0001_initial')
    ]
    
    operations = [
    migrations.RunPython(BlogEntries)
    ]
    

