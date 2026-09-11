#!/usr/bin/env python3
"""Generate the corrected multilingual TerraHit static website."""

from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASE = "https://terrahitb2b.com"
FAVICON_DATA = "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NCA2NCI+CiAgPGNpcmNsZSBjeD0iMzIiIGN5PSIzMiIgcj0iMzAiIGZpbGw9IiMwYjJmNjMiLz4KICA8Y2lyY2xlIGN4PSIzMSIgY3k9IjMxIiByPSIxOSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjZmZmZmZmIiBzdHJva2Utd2lkdGg9IjMiLz4KICA8cGF0aCBkPSJNMTIgMzFoMzhNMzEgMTJ2MzhNMTcgMjFjOCA1IDIwIDUgMjggME0xNyA0MWM3LTQgMTctNSAyNS0yTTMxIDEyYy03IDYtMTAgMTMtMTAgMTlzMyAxNCAxMCAxOU0zMSAxMmM3IDYgMTAgMTMgMTAgMTkgMCAzLS43IDYtMiA5IiBmaWxsPSJub25lIiBzdHJva2U9IiNmZmZmZmYiIHN0cm9rZS13aWR0aD0iMi41IiBzdHJva2UtbGluZWNhcD0icm91bmQiLz4KICA8cGF0aCBkPSJNMzggNDhjMi0xMCA4LTE1IDE3LTE2LTEgMTAtNiAxNi0xNyAxNloiIGZpbGw9IiMwMGE2NWEiLz4KICA8cGF0aCBkPSJNNDAgNDZjNC00IDgtNyAxMy0xMSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjZmZmZmZmIiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIvPgo8L3N2Zz4K"

LANGS = {
    "en": {"prefix": "", "dir": "ltr", "label": "English"},
    "fr": {"prefix": "/fr", "dir": "ltr", "label": "Français"},
    "ar": {"prefix": "/ar", "dir": "rtl", "label": "العربية"},
}

PAGES = {
    "home": "index.html",
    "about": "about.html",
    "services": "services.html",
    "contact": "contact.html",
    "thanks": "thank-you.html",
    "legal": "legal.html",
    "privacy": "privacy.html",
}

COPY = {
    "en": {
        "skip": "Skip to content",
        "menu": "Menu",
        "languages": "Languages",
        "nav": {"home": "Home", "about": "About", "services": "Services", "contact": "Contact", "legal": "Legal", "privacy": "Privacy"},
        "titles": {
            "home": "TerraHit LLC — Algeria–Europe Trade Coordination",
            "about": "About TerraHit — Algeria–Europe Trade Coordination",
            "services": "Trade Coordination Services — TerraHit LLC",
            "contact": "Contact TerraHit LLC",
            "thanks": "Thank You — TerraHit LLC",
            "legal": "Legal Notices — TerraHit LLC",
            "privacy": "Privacy Policy — TerraHit LLC",
        },
        "descriptions": {
            "home": "TerraHit coordinates B2B import-export operations between Algeria and Europe: supplier liaison, commercial documentation, freight-forwarder coordination and operational follow-up.",
            "about": "Learn how TerraHit LLC coordinates reliable and transparent B2B trade operations between Algeria, Europe and international markets.",
            "services": "Supplier liaison, trade documentation, logistics coordination and operational follow-up for Algeria–Europe B2B transactions.",
            "contact": "Discuss an Algeria–Europe import-export operation with TerraHit LLC.",
            "thanks": "Confirmation that your message has been sent to TerraHit LLC.",
            "legal": "Legal notices for the TerraHit LLC website.",
            "privacy": "How TerraHit LLC processes personal data submitted through its website.",
        },
        "cta": "Discuss your operation",
        "footer": "Trade coordination between Algeria and Europe",
        "home": {
            "eyebrow": "ALGERIA–EUROPE B2B TRADE",
            "h1": "Your operational bridge between Algeria and Europe",
            "h1_lines": ["Your operational bridge", "between Algeria and Europe"],
            "lead": "TerraHit coordinates suppliers, buyers, documentation and logistics partners so every party has a clear view of the operation.",
            "primary": "Describe your operation",
            "secondary": "Explore our services",
            "promise_title": "One coordinator. A clearer operation.",
            "promise": "TerraHit acts as a coordination service provider. We connect the commercial and operational stakeholders without replacing the importer of record or regulated professionals.",
            "benefits": [
                ("Supplier & buyer liaison", "A single point of contact to align needs, availability, specifications and timing."),
                ("Document coordination", "Structured follow-up of commercial and operational documents required by the transaction."),
                ("Logistics interface", "Coordination with freight forwarders and other authorised professionals through to delivery."),
            ],
            "process_title": "How we coordinate your operation",
            "process": [
                ("01", "Define", "Products, volumes, specifications, destination and target timeline."),
                ("02", "Coordinate", "Suppliers, buyer, documentation and logistics partners are aligned."),
                ("03", "Follow through", "Milestones, issues and decisions are tracked until completion."),
            ],
            "scope_title": "A focused operating corridor",
            "scope": "Our primary expertise is the Algeria–France/EU corridor, with an initial focus on agri-food operations and the ability to evaluate other products on a case-by-case basis.",
            "closing_title": "Have an operation to structure?",
            "closing": "Tell us the product, origin, destination, volume and desired timing. We will assess the coordination required.",
        },
        "about": {
            "h1": "About TerraHit",
            "intro": "TerraHit LLC is a New Mexico company providing commercial, documentary and logistics coordination for cross-border B2B operations.",
            "sections": [
                ("Our role", "We provide an operational interface between suppliers, buyers, freight forwarders and other authorised professionals. Our goal is to make responsibilities, information and milestones clear throughout the transaction."),
                ("Our mission", "To make Algeria–Europe trade operations easier to structure and follow through reliable coordination, transparent communication and disciplined execution."),
                ("Our approach", "We begin with the real parameters of the operation—product, quantity, specifications, destination, documents and timing—then coordinate the relevant parties around a shared operational plan."),
            ],
            "values_title": "Our principles",
            "values": [
                ("Transparency", "Clear roles, costs, documents and decisions."),
                ("Reliability", "Consistent follow-up and early escalation of issues."),
                ("Pragmatism", "Solutions adapted to the actual operation."),
                ("Partnership", "Long-term relationships built around shared results."),
            ],
        },
        "services": {
            "h1": "Trade coordination services",
            "intro": "Modular support adapted to the needs of each Algeria–Europe operation.",
            "cards": [
                ("Commercial scoping", "Clarification of products, specifications, quantities, price structure, counterparties and transaction milestones."),
                ("Supplier and buyer liaison", "Coordination of information and decisions between the commercial parties."),
                ("Documentation follow-up", "Operational follow-up of quotations, invoices, packing lists, certificates and other transaction documents."),
                ("Logistics coordination", "Interface with freight forwarders, handlers and authorised customs or inspection professionals."),
                ("Operational monitoring", "Tracking of deadlines, document status, incidents and actions until completion."),
                ("Partner introduction", "Identification and introduction of relevant commercial or logistics partners when appropriate."),
            ],
            "boundary_title": "A clearly defined role",
            "boundary": "TerraHit provides coordination and commercial support. Unless expressly agreed and legally authorised, TerraHit is not the seller of the goods, the importer of record, a customs representative, a carrier or a legal/tax adviser. Regulated formalities remain under the responsibility of the relevant authorised professionals and contracting parties.",
        },
        "contact": {
            "h1": "Discuss your operation",
            "intro": "Share the essential parameters. We will respond with the next information needed to assess the project.",
            "info": "Contact information",
            "hq": "Registered office",
            "operations": "Primary operating area",
            "operations_value": "Algeria, France and the European Union",
            "name": "Full name",
            "company": "Company",
            "email": "Business email",
            "type": "Type of request",
            "select": "Select…",
            "options": [("trade", "Trade operation scoping"), ("supplier", "Supplier or buyer liaison"), ("documents", "Documentation coordination"), ("logistics", "Logistics coordination"), ("other", "Other")],
            "message": "Operation details",
            "message_help": "Product, origin, destination, estimated volume and desired timing.",
            "submit": "Send request",
            "sending": "Sending…",
            "error": "Your message could not be sent. Please try again or email contact@terrahitb2b.com.",
            "privacy_note": "TerraHit uses the information provided solely to review and respond to your request.",
            "privacy_link": "Read the privacy policy",
        },
        "thanks": {
            "h1": "Thank you for your message",
            "intro": "Your request has been sent to TerraHit.",
            "message": "We will review the information provided and contact you if further details are needed.",
            "home": "Return to the homepage",
            "contact": "Send another request",
        },
        "legal": {
            "h1": "Legal notices",
            "blocks": [
                ("1. Publisher", "<strong>TerraHit LLC</strong><br>Limited Liability Company<br>2105 Vista Oeste NW, Suite E #2030<br>Albuquerque, NM 87120, United States<br>Email: <a href=\"mailto:contact@terrahitb2b.com\">contact@terrahitb2b.com</a>"),
                ("2. Hosting and infrastructure", "The website is hosted using GitHub Pages infrastructure. Cloudflare services may be used for DNS, content delivery, security and traffic protection."),
                ("3. Website purpose", "This website presents TerraHit LLC and its coordination services. Its content is informational and does not constitute a binding commercial, legal, customs or tax offer."),
                ("4. Scope of services", "TerraHit coordinates commercial, documentary and logistics stakeholders. Regulated activities and formalities are performed by the contracting parties or appropriately authorised professionals."),
                ("5. Intellectual property", "Unless otherwise stated, the TerraHit name, logo, design and original website content are owned by TerraHit LLC or used with permission."),
                ("6. Liability", "TerraHit LLC takes reasonable care in publishing information but does not guarantee that every item remains complete or current. Specific commitments arise only from a written agreement."),
                ("7. Governing law", "These website notices are governed by the laws applicable to TerraHit LLC, without limiting mandatory rules that may apply to a particular user or commercial transaction."),
                ("8. Contact", "Questions concerning this website may be sent to <a href=\"mailto:contact@terrahitb2b.com\">contact@terrahitb2b.com</a>."),
            ],
            "updated": "Last updated: September 2026",
        },
        "privacy": {
            "h1": "Privacy policy",
            "blocks": [
                ("1. Data controller", "TerraHit LLC, 2105 Vista Oeste NW, Suite E #2030, Albuquerque, NM 87120, United States. Contact: <a href=\"mailto:contact@terrahitb2b.com\">contact@terrahitb2b.com</a>."),
                ("2. Data collected", "The contact form collects your name, company, business email, request type and message. Technical security logs may also include an IP address, browser information and access time."),
                ("3. Purposes and legal basis", "Contact data is processed to assess and answer your request, take pre-contractual steps at your request, manage a potential business relationship and protect the website. Technical logs are processed for security and service reliability."),
                ("4. Recipients and processors", "Access is limited to TerraHit personnel who need the information and service providers involved in operating the website and handling the form. Form submissions are transmitted through Basin (usebasin.com). GitHub Pages and Cloudflare may process limited technical data required to deliver and secure the website."),
                ("5. International processing", "TerraHit operates from the United States and website providers may process data outside the European Economic Area. You may contact TerraHit for information about the safeguards applicable to a particular transfer."),
                ("6. Retention", "Unsuccessful initial enquiries are normally retained for no more than 12 months after the last exchange. Records connected with a contract are retained for the period required to manage the relationship and comply with legal, accounting and dispute-resolution obligations. Security logs are retained only as long as necessary for security purposes."),
                ("7. Your rights", "Subject to applicable law, you may request access, correction, deletion, restriction or objection, and data portability where relevant. You may also complain to the competent data-protection authority. Send requests to <a href=\"mailto:contact@terrahitb2b.com\">contact@terrahitb2b.com</a>."),
                ("8. Cookies", "The website does not intentionally use advertising or behavioural analytics cookies. Essential technical measures may be used to deliver, secure and remember the language or interface requested by the user. This notice will be updated before any non-essential tracking technology is introduced."),
                ("9. Security and updates", "Reasonable technical and organisational safeguards are used to protect data. This policy may be updated to reflect changes in services or legal requirements."),
            ],
            "updated": "Last updated: September 2026",
        },
    },
    "fr": {
        "skip": "Aller au contenu",
        "menu": "Menu",
        "languages": "Langues",
        "nav": {"home": "Accueil", "about": "À propos", "services": "Services", "contact": "Contact", "legal": "Mentions légales", "privacy": "Confidentialité"},
        "titles": {
            "home": "TerraHit LLC — Coordination commerciale Algérie–Europe",
            "about": "À propos de TerraHit — Coordination Algérie–Europe",
            "services": "Services de coordination commerciale — TerraHit LLC",
            "contact": "Contacter TerraHit LLC",
            "thanks": "Merci pour votre message — TerraHit LLC",
            "legal": "Mentions légales — TerraHit LLC",
            "privacy": "Politique de confidentialité — TerraHit LLC",
        },
        "descriptions": {
            "home": "TerraHit coordonne les opérations B2B entre l’Algérie et l’Europe : fournisseurs, documentation commerciale, transitaires et suivi opérationnel.",
            "about": "Découvrez comment TerraHit LLC coordonne des opérations commerciales B2B fiables et transparentes entre l’Algérie et l’Europe.",
            "services": "Mise en relation, coordination documentaire et logistique, et suivi opérationnel des échanges B2B Algérie–Europe.",
            "contact": "Présentez votre opération d’import-export Algérie–Europe à TerraHit LLC.",
            "thanks": "Confirmation de l’envoi de votre message à TerraHit LLC.",
            "legal": "Mentions légales du site TerraHit LLC.",
            "privacy": "Informations sur le traitement des données personnelles par TerraHit LLC.",
        },
        "cta": "Présenter votre opération",
        "footer": "Coordination commerciale entre l’Algérie et l’Europe",
        "home": {
            "eyebrow": "COMMERCE B2B ALGÉRIE–EUROPE",
            "h1": "Votre passerelle opérationnelle entre l’Algérie et l’Europe",
            "h1_lines": ["Votre passerelle opérationnelle", "entre l’Algérie et l’Europe"],
            "lead": "TerraHit coordonne fournisseurs, acheteurs, documentation et partenaires logistiques afin que chaque intervenant dispose d’une vision claire de l’opération.",
            "primary": "Présenter votre opération",
            "secondary": "Découvrir nos services",
            "promise_title": "Un coordinateur. Une opération plus lisible.",
            "promise": "TerraHit intervient comme prestataire de coordination. Nous relions les acteurs commerciaux et opérationnels sans nous substituer à l’importateur officiel ni aux professionnels réglementés.",
            "benefits": [
                ("Liaison fournisseurs–acheteurs", "Un interlocuteur unique pour aligner besoins, disponibilités, spécifications et calendrier."),
                ("Coordination documentaire", "Suivi structuré des documents commerciaux et opérationnels nécessaires à la transaction."),
                ("Interface logistique", "Coordination avec les transitaires et autres professionnels autorisés jusqu’à la livraison."),
            ],
            "process_title": "Comment nous coordonnons votre opération",
            "process": [
                ("01", "Définir", "Produits, volumes, spécifications, destination et calendrier cible."),
                ("02", "Coordonner", "Fournisseurs, acheteur, documents et partenaires logistiques sont alignés."),
                ("03", "Suivre", "Les étapes, incidents et décisions sont suivis jusqu’à l’achèvement."),
            ],
            "scope_title": "Un corridor opérationnel maîtrisé",
            "scope": "Notre expertise principale porte sur le corridor Algérie–France/UE, d’abord pour les opérations agroalimentaires, avec étude d’autres produits au cas par cas.",
            "closing_title": "Une opération à structurer ?",
            "closing": "Indiquez le produit, l’origine, la destination, le volume et le calendrier souhaité. Nous évaluerons la coordination nécessaire.",
        },
        "about": {
            "h1": "À propos de TerraHit",
            "intro": "TerraHit LLC est une société du Nouveau-Mexique spécialisée dans la coordination commerciale, documentaire et logistique d’opérations B2B transfrontalières.",
            "sections": [
                ("Notre rôle", "Nous assurons l’interface opérationnelle entre fournisseurs, acheteurs, transitaires et autres professionnels autorisés. Notre objectif est de rendre les responsabilités, les informations et les échéances lisibles tout au long de la transaction."),
                ("Notre mission", "Faciliter la structuration et le suivi des échanges Algérie–Europe grâce à une coordination fiable, une communication transparente et une exécution rigoureuse."),
                ("Notre méthode", "Nous partons des paramètres réels de l’opération — produit, quantité, spécifications, destination, documents et calendrier — puis coordonnons les intervenants autour d’un plan opérationnel partagé."),
            ],
            "values_title": "Nos principes",
            "values": [("Transparence", "Des rôles, coûts, documents et décisions clairement identifiés."), ("Fiabilité", "Un suivi constant et une remontée rapide des difficultés."), ("Pragmatisme", "Des solutions adaptées à l’opération réelle."), ("Partenariat", "Des relations durables construites autour de résultats partagés.")],
        },
        "services": {
            "h1": "Services de coordination commerciale",
            "intro": "Un accompagnement modulable selon les besoins de chaque opération Algérie–Europe.",
            "cards": [
                ("Cadrage commercial", "Clarification des produits, spécifications, quantités, structure de prix, contreparties et étapes de la transaction."),
                ("Liaison fournisseurs–acheteurs", "Coordination des informations et décisions entre les parties commerciales."),
                ("Suivi documentaire", "Suivi opérationnel des devis, factures, listes de colisage, certificats et autres documents de la transaction."),
                ("Coordination logistique", "Interface avec les transitaires, manutentionnaires et professionnels autorisés de la douane ou du contrôle."),
                ("Suivi opérationnel", "Suivi des échéances, documents, incidents et actions jusqu’à l’achèvement."),
                ("Mise en relation", "Identification et présentation de partenaires commerciaux ou logistiques pertinents lorsque nécessaire."),
            ],
            "boundary_title": "Un rôle clairement défini",
            "boundary": "TerraHit fournit des services de coordination et d’appui commercial. Sauf accord exprès et autorisation légale, TerraHit n’est ni le vendeur des marchandises, ni l’importateur officiel, ni un représentant en douane, un transporteur ou un conseil juridique ou fiscal. Les formalités réglementées restent sous la responsabilité des professionnels autorisés et des parties contractantes concernées.",
        },
        "contact": {
            "h1": "Présentez votre opération",
            "intro": "Transmettez les paramètres essentiels. Nous vous indiquerons les informations complémentaires nécessaires à l’étude du projet.",
            "info": "Coordonnées",
            "hq": "Siège social",
            "operations": "Zone d’intervention principale",
            "operations_value": "Algérie, France et Union européenne",
            "name": "Nom complet",
            "company": "Entreprise",
            "email": "E-mail professionnel",
            "type": "Type de demande",
            "select": "Sélectionner…",
            "options": [("trade", "Cadrage d’une opération commerciale"), ("supplier", "Liaison fournisseur ou acheteur"), ("documents", "Coordination documentaire"), ("logistics", "Coordination logistique"), ("other", "Autre")],
            "message": "Détails de l’opération",
            "message_help": "Produit, origine, destination, volume estimé et calendrier souhaité.",
            "submit": "Envoyer la demande",
            "sending": "Envoi en cours…",
            "error": "Votre message n’a pas pu être envoyé. Réessayez ou écrivez à contact@terrahitb2b.com.",
            "privacy_note": "TerraHit utilise les informations fournies uniquement pour étudier votre demande et vous répondre.",
            "privacy_link": "Consulter la politique de confidentialité",
        },
        "thanks": {
            "h1": "Merci pour votre message",
            "intro": "Votre demande a bien été transmise à TerraHit.",
            "message": "Nous allons examiner les informations communiquées et vous contacter si des précisions sont nécessaires.",
            "home": "Retour à l’accueil",
            "contact": "Envoyer une autre demande",
        },
        "legal": {
            "h1": "Mentions légales",
            "blocks": [
                ("1. Éditeur", "<strong>TerraHit LLC</strong><br>Limited Liability Company<br>2105 Vista Oeste NW, Suite E #2030<br>Albuquerque, NM 87120, États-Unis<br>E-mail : <a href=\"mailto:contact@terrahitb2b.com\">contact@terrahitb2b.com</a>"),
                ("2. Hébergement et infrastructure", "Le site est hébergé au moyen de l’infrastructure GitHub Pages. Des services Cloudflare peuvent être utilisés pour le DNS, la diffusion des contenus, la sécurité et la protection du trafic."),
                ("3. Objet du site", "Ce site présente TerraHit LLC et ses services de coordination. Son contenu est informatif et ne constitue pas une offre commerciale, juridique, douanière ou fiscale ferme."),
                ("4. Périmètre des services", "TerraHit coordonne les intervenants commerciaux, documentaires et logistiques. Les activités et formalités réglementées sont accomplies par les parties contractantes ou des professionnels dûment autorisés."),
                ("5. Propriété intellectuelle", "Sauf indication contraire, le nom TerraHit, le logo, la conception et les contenus originaux du site appartiennent à TerraHit LLC ou sont utilisés avec autorisation."),
                ("6. Responsabilité", "TerraHit LLC apporte un soin raisonnable aux informations publiées, sans garantir qu’elles demeurent en permanence complètes ou à jour. Seul un accord écrit crée des engagements spécifiques."),
                ("7. Droit applicable", "Les présentes mentions sont soumises aux règles applicables à TerraHit LLC, sans limiter les dispositions impératives pouvant s’appliquer à un utilisateur ou à une transaction particulière."),
                ("8. Contact", "Toute question relative au site peut être adressée à <a href=\"mailto:contact@terrahitb2b.com\">contact@terrahitb2b.com</a>."),
            ],
            "updated": "Dernière mise à jour : septembre 2026",
        },
        "privacy": {
            "h1": "Politique de confidentialité",
            "blocks": [
                ("1. Responsable du traitement", "TerraHit LLC, 2105 Vista Oeste NW, Suite E #2030, Albuquerque, NM 87120, États-Unis. Contact : <a href=\"mailto:contact@terrahitb2b.com\">contact@terrahitb2b.com</a>."),
                ("2. Données collectées", "Le formulaire recueille votre nom, votre entreprise, votre e-mail professionnel, le type de demande et votre message. Les journaux techniques de sécurité peuvent également contenir l’adresse IP, des informations sur le navigateur et l’heure d’accès."),
                ("3. Finalités et bases juridiques", "Les données de contact servent à étudier et traiter votre demande, accomplir à votre initiative des mesures précontractuelles, gérer une éventuelle relation commerciale et protéger le site. Les journaux techniques sont traités pour la sécurité et la fiabilité du service."),
                ("4. Destinataires et prestataires", "L’accès est limité aux personnes de TerraHit qui en ont besoin et aux prestataires nécessaires au fonctionnement du site et du formulaire. Les demandes sont transmises par Basin (usebasin.com). GitHub Pages et Cloudflare peuvent traiter les données techniques strictement nécessaires à la diffusion et à la sécurisation du site."),
                ("5. Traitements internationaux", "TerraHit opère depuis les États-Unis et certains prestataires peuvent traiter des données en dehors de l’Espace économique européen. Vous pouvez contacter TerraHit pour obtenir des informations sur les garanties applicables à un transfert particulier."),
                ("6. Conservation", "Les demandes initiales n’ayant pas abouti sont normalement conservées au maximum douze mois après le dernier échange. Les données liées à un contrat sont conservées pendant la durée nécessaire à la relation et au respect des obligations légales, comptables et contentieuses. Les journaux de sécurité ne sont conservés que pendant la durée nécessaire à la sécurité."),
                ("7. Vos droits", "Sous réserve du droit applicable, vous pouvez demander l’accès, la rectification, l’effacement, la limitation ou l’opposition, ainsi que la portabilité lorsqu’elle est pertinente. Vous pouvez également saisir l’autorité de protection des données compétente. Adressez vos demandes à <a href=\"mailto:contact@terrahitb2b.com\">contact@terrahitb2b.com</a>."),
                ("8. Cookies", "Le site n’utilise volontairement aucun cookie publicitaire ni traceur d’analyse comportementale. Des mesures techniques indispensables peuvent être utilisées pour diffuser et sécuriser le site ou mémoriser une langue ou une présentation demandée par l’utilisateur. Cette politique sera mise à jour avant l’ajout de tout traceur non essentiel."),
                ("9. Sécurité et mises à jour", "Des mesures techniques et organisationnelles raisonnables sont mises en œuvre pour protéger les données. La présente politique peut évoluer selon les services utilisés ou les exigences légales."),
            ],
            "updated": "Dernière mise à jour : septembre 2026",
        },
    },
    "ar": {
        "skip": "الانتقال إلى المحتوى",
        "menu": "القائمة",
        "languages": "اللغات",
        "nav": {"home": "الرئيسية", "about": "من نحن", "services": "خدماتنا", "contact": "اتصل بنا", "legal": "إشعار قانوني", "privacy": "الخصوصية"},
        "titles": {"home": "TerraHit LLC — تنسيق التجارة بين الجزائر وأوروبا", "about": "من نحن — TerraHit LLC", "services": "خدمات تنسيق التجارة — TerraHit LLC", "contact": "اتصل بـ TerraHit LLC", "thanks": "شكراً لرسالتك — TerraHit LLC", "legal": "الإشعار القانوني — TerraHit LLC", "privacy": "سياسة الخصوصية — TerraHit LLC"},
        "descriptions": {
            "home": "تنسق TerraHit عمليات التجارة بين الشركات في الجزائر وأوروبا، بما يشمل التواصل مع الموردين والوثائق التجارية والشحن والمتابعة التشغيلية.",
            "about": "تعرّف على دور TerraHit LLC في تنسيق عمليات تجارية موثوقة وشفافة بين الجزائر وأوروبا.",
            "services": "تنسيق الموردين والوثائق والخدمات اللوجستية والمتابعة التشغيلية للتجارة بين الجزائر وأوروبا.",
            "contact": "اعرض مشروع الاستيراد أو التصدير بين الجزائر وأوروبا على TerraHit LLC.",
            "thanks": "تأكيد إرسال رسالتك إلى TerraHit LLC.",
            "legal": "الإشعار القانوني لموقع TerraHit LLC.",
            "privacy": "كيفية معالجة TerraHit LLC للبيانات الشخصية المقدمة عبر موقعها.",
        },
        "cta": "اعرض عمليتك",
        "footer": "تنسيق التجارة بين الجزائر وأوروبا",
        "home": {
            "eyebrow": "التجارة بين الشركات — الجزائر وأوروبا",
            "h1": "جسرك التشغيلي بين الجزائر وأوروبا",
            "h1_lines": ["جسرك التشغيلي", "بين الجزائر وأوروبا"],
            "lead": "تنسق TerraHit بين الموردين والمشترين والوثائق والشركاء اللوجستيين، بما يضمن وضوح العملية لجميع الأطراف.",
            "primary": "اعرض عمليتك",
            "secondary": "اكتشف خدماتنا",
            "promise_title": "منسّق واحد. عملية أكثر وضوحًا.",
            "promise": "تقدم TerraHit خدمة تنسيق تربط بين الأطراف التجارية والتشغيلية، من دون أن تحل محل المستورد الرسمي أو المهنيين المعتمدين.",
            "benefits": [("التنسيق بين المورد والمشتري", "نقطة اتصال واحدة لتنسيق الاحتياجات والتوفر والمواصفات والمواعيد."), ("متابعة الوثائق", "متابعة منظمة للوثائق التجارية والتشغيلية اللازمة للمعاملة."), ("الواجهة اللوجستية", "التنسيق مع وكلاء الشحن وغيرهم من المهنيين المعتمدين حتى التسليم.")],
            "process_title": "كيف ننسق عمليتك",
            "process": [("01", "التحديد", "المنتجات والكميات والمواصفات والوجهة والجدول الزمني."), ("02", "التنسيق", "تنسيق المورد والمشتري والوثائق والشركاء اللوجستيين."), ("03", "المتابعة", "متابعة المراحل والصعوبات والقرارات إلى غاية إتمام العملية.")],
            "scope_title": "محور تجاري واضح",
            "scope": "تتركز خبرتنا الأساسية على محور الجزائر–فرنسا/الاتحاد الأوروبي، بدءًا من العمليات الغذائية والزراعية، مع دراسة المنتجات الأخرى حسب كل حالة.",
            "closing_title": "لديك عملية تحتاج إلى تنظيم؟",
            "closing": "اذكر المنتج والمنشأ والوجهة والحجم والموعد المطلوب، وسنقيّم احتياجات التنسيق.",
        },
        "about": {
            "h1": "من نحن",
            "intro": "TerraHit LLC شركة مسجلة في ولاية نيو مكسيكو، متخصصة في التنسيق التجاري والوثائقي واللوجستي للعمليات الدولية بين الشركات.",
            "sections": [("دورنا", "نؤمّن الواجهة التشغيلية بين الموردين والمشترين ووكلاء الشحن وغيرهم من المهنيين المعتمدين، بهدف توضيح المسؤوليات والمعلومات والمواعيد طوال العملية."), ("مهمتنا", "تسهيل تنظيم ومتابعة التجارة بين الجزائر وأوروبا عبر تنسيق موثوق وتواصل شفاف وتنفيذ منضبط."), ("منهجنا", "ننطلق من المعطيات الفعلية للعملية — المنتج والكمية والمواصفات والوجهة والوثائق والجدول الزمني — ثم ننسق بين الأطراف وفق خطة تشغيلية مشتركة.")],
            "values_title": "مبادئنا",
            "values": [("الشفافية", "وضوح الأدوار والتكاليف والوثائق والقرارات."), ("الموثوقية", "متابعة مستمرة والتنبيه المبكر إلى الصعوبات."), ("الواقعية", "حلول تناسب العملية الفعلية."), ("الشراكة", "علاقات طويلة الأمد مبنية على نتائج مشتركة.")],
        },
        "services": {
            "h1": "خدمات تنسيق التجارة",
            "intro": "دعم مرن يتكيف مع احتياجات كل عملية بين الجزائر وأوروبا.",
            "cards": [("تحديد الإطار التجاري", "توضيح المنتجات والمواصفات والكميات وهيكل الأسعار والأطراف ومراحل المعاملة."), ("التنسيق بين المورد والمشتري", "تنسيق المعلومات والقرارات بين الأطراف التجارية."), ("متابعة الوثائق", "متابعة عروض الأسعار والفواتير وقوائم التعبئة والشهادات وغيرها من وثائق المعاملة."), ("التنسيق اللوجستي", "التواصل مع وكلاء الشحن والمناولة والمتخصصين المعتمدين في الجمارك أو المراقبة."), ("المتابعة التشغيلية", "متابعة المواعيد والوثائق والصعوبات والإجراءات حتى إتمام العملية."), ("ربط الشركاء", "تحديد وتقديم الشركاء التجاريين أو اللوجستيين المناسبين عند الحاجة.")],
            "boundary_title": "دور محدد بوضوح",
            "boundary": "تقدم TerraHit خدمات التنسيق والدعم التجاري. وما لم يوجد اتفاق صريح وترخيص قانوني، فهي ليست بائع البضاعة ولا المستورد الرسمي ولا ممثلًا جمركيًا أو ناقلًا أو مستشارًا قانونيًا أو ضريبيًا. وتبقى الإجراءات المنظمة من مسؤولية المهنيين المعتمدين والأطراف المتعاقدة المعنية.",
        },
        "contact": {
            "h1": "اعرض عمليتك",
            "intro": "أرسل المعلومات الأساسية وسنحدد البيانات الإضافية اللازمة لدراسة المشروع.",
            "info": "معلومات الاتصال",
            "hq": "المقر المسجل",
            "operations": "منطقة العمل الأساسية",
            "operations_value": "الجزائر وفرنسا والاتحاد الأوروبي",
            "name": "الاسم الكامل",
            "company": "الشركة",
            "email": "البريد الإلكتروني المهني",
            "type": "نوع الطلب",
            "select": "اختر…",
            "options": [("trade", "تحديد إطار عملية تجارية"), ("supplier", "التنسيق مع مورد أو مشترٍ"), ("documents", "تنسيق الوثائق"), ("logistics", "التنسيق اللوجستي"), ("other", "أخرى")],
            "message": "تفاصيل العملية",
            "message_help": "المنتج والمنشأ والوجهة والحجم التقريبي والموعد المطلوب.",
            "submit": "إرسال الطلب",
            "sending": "جارٍ الإرسال…",
            "error": "تعذر إرسال رسالتك. حاول مرة أخرى أو راسل contact@terrahitb2b.com.",
            "privacy_note": "تستخدم TerraHit المعلومات المقدمة فقط لدراسة طلبك والرد عليه.",
            "privacy_link": "اطلع على سياسة الخصوصية",
        },
        "thanks": {
            "h1": "شكراً لرسالتك",
            "intro": "تم إرسال طلبك إلى TerraHit بنجاح.",
            "message": "سنراجع المعلومات المقدمة ونتواصل معك إذا احتجنا إلى تفاصيل إضافية.",
            "home": "العودة إلى الصفحة الرئيسية",
            "contact": "إرسال طلب آخر",
        },
        "legal": {
            "h1": "الإشعار القانوني",
            "blocks": [("1. ناشر الموقع", "<strong>TerraHit LLC</strong><br>شركة ذات مسؤولية محدودة<br>2105 Vista Oeste NW, Suite E #2030<br>Albuquerque, NM 87120, United States<br>البريد الإلكتروني: <a href=\"mailto:contact@terrahitb2b.com\">contact@terrahitb2b.com</a>"), ("2. الاستضافة والبنية التحتية", "يستضاف الموقع عبر بنية GitHub Pages، وقد تُستخدم خدمات Cloudflare لإدارة النطاق وتوزيع المحتوى والأمن وحماية حركة المرور."), ("3. غرض الموقع", "يعرّف هذا الموقع بشركة TerraHit LLC وخدمات التنسيق التي تقدمها. والمحتوى إعلامي ولا يمثل عرضًا تجاريًا أو قانونيًا أو جمركيًا أو ضريبيًا ملزمًا."), ("4. نطاق الخدمات", "تنسق TerraHit بين الأطراف التجارية والوثائقية واللوجستية، بينما تنجز الأنشطة والإجراءات المنظمة من قبل الأطراف المتعاقدة أو المهنيين المعتمدين."), ("5. الملكية الفكرية", "ما لم يُذكر خلاف ذلك، فإن اسم TerraHit وشعارها وتصميم الموقع ومحتواه الأصلي مملوك للشركة أو مستخدم بإذن."), ("6. المسؤولية", "تبذل TerraHit LLC عناية معقولة في نشر المعلومات، لكنها لا تضمن بقاء جميع المعلومات كاملة أو محدثة في كل وقت. ولا تنشأ الالتزامات الخاصة إلا بموجب اتفاق مكتوب."), ("7. القانون الواجب التطبيق", "تخضع هذه الإشعارات للقواعد المطبقة على TerraHit LLC، مع عدم المساس بالقواعد الإلزامية التي قد تنطبق على مستخدم أو معاملة معينة."), ("8. الاتصال", "يمكن إرسال الأسئلة المتعلقة بالموقع إلى <a href=\"mailto:contact@terrahitb2b.com\">contact@terrahitb2b.com</a>. ")],
            "updated": "آخر تحديث: سبتمبر 2026",
        },
        "privacy": {
            "h1": "سياسة الخصوصية",
            "blocks": [("1. مسؤول معالجة البيانات", "TerraHit LLC، 2105 Vista Oeste NW, Suite E #2030, Albuquerque, NM 87120, United States. الاتصال: <a href=\"mailto:contact@terrahitb2b.com\">contact@terrahitb2b.com</a>."), ("2. البيانات المجمعة", "يجمع نموذج الاتصال الاسم والشركة والبريد الإلكتروني المهني ونوع الطلب والرسالة. وقد تتضمن سجلات الأمان التقنية عنوان IP ومعلومات المتصفح ووقت الدخول."), ("3. الأغراض والأساس القانوني", "تستخدم بيانات الاتصال لدراسة الطلب والرد عليه واتخاذ إجراءات ما قبل التعاقد بناءً على طلبك وإدارة علاقة تجارية محتملة وحماية الموقع. وتعالج السجلات التقنية لأغراض الأمان وموثوقية الخدمة."), ("4. المستلمون ومقدمو الخدمة", "يقتصر الوصول على الأشخاص المعنيين داخل TerraHit ومقدمي الخدمات اللازمين لتشغيل الموقع والنموذج. ترسل الطلبات عبر Basin (usebasin.com)، وقد تعالج GitHub Pages وCloudflare بيانات تقنية محدودة لازمة لتقديم الموقع وتأمينه."), ("5. المعالجة الدولية", "تعمل TerraHit من الولايات المتحدة، وقد يعالج بعض مقدمي الخدمات البيانات خارج المنطقة الاقتصادية الأوروبية. ويمكنك التواصل معنا للحصول على معلومات عن الضمانات المطبقة على أي نقل معين."), ("6. مدة الاحتفاظ", "تُحفظ الطلبات الأولية التي لا تؤدي إلى تعاقد لمدة لا تتجاوز عادةً اثني عشر شهرًا بعد آخر تواصل. وتُحفظ البيانات المرتبطة بعقد للمدة اللازمة لإدارة العلاقة والامتثال للالتزامات القانونية والمحاسبية وتسوية النزاعات."), ("7. حقوقك", "وفقًا للقانون المطبق، يمكنك طلب الوصول أو التصحيح أو المحو أو تقييد المعالجة أو الاعتراض، وطلب نقل البيانات عند الاقتضاء. كما يمكنك تقديم شكوى إلى سلطة حماية البيانات المختصة. أرسل طلبك إلى <a href=\"mailto:contact@terrahitb2b.com\">contact@terrahitb2b.com</a>."), ("8. ملفات تعريف الارتباط", "لا يستخدم الموقع عمدًا ملفات تعريف ارتباط إعلانية أو أدوات تحليل سلوكي. وقد تستخدم تدابير تقنية ضرورية لتقديم الموقع وتأمينه أو حفظ اللغة أو الواجهة التي يطلبها المستخدم."), ("9. الأمان والتحديثات", "تُستخدم تدابير تقنية وتنظيمية معقولة لحماية البيانات، وقد تُحدّث هذه السياسة عند تغير الخدمات أو المتطلبات القانونية.")],
            "updated": "آخر تحديث: سبتمبر 2026",
        },
    },
}


def href(lang: str, page: str) -> str:
    prefix = LANGS[lang]["prefix"]
    filename = PAGES[page]
    if page == "home":
        return f"{prefix}/" if prefix else "/"
    return f"{prefix}/{filename}" if prefix else f"/{filename}"


def canonical(lang: str, page: str) -> str:
    return BASE + href(lang, page)


def language_links(page: str) -> str:
    return "\n".join(
        f'<link rel="alternate" hreflang="{code}" href="{canonical(code, page)}">'
        for code in LANGS
    ) + f'\n<link rel="alternate" hreflang="x-default" href="{canonical("en", page)}">'


def language_redirect(lang: str, page: str) -> str:
    if lang != "en":
        return ""
    return f'''<script>
  (function () {{
    try {{
      var saved = localStorage.getItem('terrahit-language');
      var detected = saved || (navigator.languages && navigator.languages[0]) || navigator.language || 'en';
      var language = detected.toLowerCase();
      var target = language.indexOf('fr') === 0 ? '{href('fr', page)}' : language.indexOf('ar') === 0 ? '{href('ar', page)}' : '';
      if (target) window.location.replace(target + window.location.search + window.location.hash);
    }} catch (error) {{}}
  }})();
</script>'''


def header(lang: str, page: str) -> str:
    copy = COPY[lang]
    nav = copy["nav"]
    links = "".join(
        f'<li><a href="{href(lang, key)}"' + (' aria-current="page"' if key == page else '') + f'>{escape(nav[key])}</a></li>'
        for key in ("home", "about", "services", "contact")
    )
    lang_links = "".join(
        f'<a href="{href(code, page)}" lang="{code}" hreflang="{code}" data-language-choice="{code}"' + (' aria-current="true"' if code == lang else '') + f'>{code.upper()}</a>'
        for code in LANGS
    )
    return f'''<header class="site-header">
  <nav class="nav-shell" aria-label="{escape('التنقل الرئيسي' if lang == 'ar' else 'Navigation principale' if lang == 'fr' else 'Main navigation')}">
    <a class="brand" href="{href(lang, 'home')}" aria-label="TerraHit — {escape(nav['home'])}"><img src="/logo_terrahit.webp?v=1" alt="TerraHit LLC" width="188" height="106" decoding="async"></a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="primary-menu"><span class="sr-only">{escape(copy['menu'])}</span><span></span><span></span><span></span></button>
    <div class="nav-panel" id="primary-menu">
      <ul>{links}</ul>
      <div class="language-switcher" aria-label="{escape(copy['languages'])}">{lang_links}</div>
      <a class="button button-small" href="{href(lang, 'contact')}">{escape(COPY[lang]['cta'])}</a>
    </div>
  </nav>
</header>'''


def footer(lang: str) -> str:
    nav = COPY[lang]["nav"]
    return f'''<footer class="site-footer">
  <div class="footer-main">
    <a class="footer-brand" href="{href(lang, 'home')}"><img src="/logo_terrahit.webp?v=1" alt="TerraHit LLC" width="188" height="106" loading="lazy" decoding="async"></a>
    <p>{escape(COPY[lang]['footer'])}</p>
    <div class="footer-links"><a href="{href(lang, 'legal')}">{escape(nav['legal'])}</a><a href="{href(lang, 'privacy')}">{escape(nav['privacy'])}</a><a href="mailto:contact@terrahitb2b.com">contact@terrahitb2b.com</a></div>
  </div>
  <p class="copyright">© 2026 TerraHit LLC</p>
</footer>'''


def base_page(lang: str, page: str, body: str) -> str:
    c = COPY[lang]
    json_ld = ""
    if page == "home":
        json_ld = '''<script type="application/ld+json">{"@context":"https://schema.org","@type":"Organization","name":"TerraHit LLC","url":"https://terrahitb2b.com/","logo":"https://terrahitb2b.com/logo_terrahit_circulaire.png","email":"contact@terrahitb2b.com","address":{"@type":"PostalAddress","streetAddress":"2105 Vista Oeste NW, Suite E #2030","addressLocality":"Albuquerque","addressRegion":"NM","postalCode":"87120","addressCountry":"US"},"areaServed":["Algeria","France","European Union"]}</script>'''
    return f'''<!doctype html>
<html lang="{lang}" dir="{LANGS[lang]['dir']}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(c['titles'][page])}</title>
  <meta name="description" content="{escape(c['descriptions'][page])}">
  <meta name="robots" content="{'noindex,follow' if page == 'thanks' else 'index,follow,max-image-preview:large'}">
  <link rel="canonical" href="{canonical(lang, page)}">
  {language_links(page)}
  <meta property="og:type" content="website">
  <meta property="og:title" content="{escape(c['titles'][page])}">
  <meta property="og:description" content="{escape(c['descriptions'][page])}">
  <meta property="og:url" content="{canonical(lang, page)}">
  <meta property="og:locale" content="{'ar_DZ' if lang == 'ar' else 'fr_FR' if lang == 'fr' else 'en_US'}">
  <meta name="twitter:card" content="summary">
  <meta name="theme-color" content="#1C2B49">
  {language_redirect(lang, page)}
  <link rel="icon" href="/favicon.ico?v=6" sizes="any">
  <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png?v=6">
  <link rel="icon" type="image/svg+xml" href="{FAVICON_DATA}">
  <link rel="apple-touch-icon" sizes="180x180" href="/favicon_512x512.png?v=6">
  <meta name="theme-color" content="#0b2f63">
  <link rel="stylesheet" href="/assets/styles.css?v=11">
  {json_ld}
</head>
<body>
  <a class="skip-link" href="#main">{escape(c['skip'])}</a>
  {header(lang, page)}
  <main id="main">{body}</main>
  {footer(lang)}
  <script src="/assets/site.js?v=6" defer></script>
</body>
</html>
'''


def home_body(lang: str) -> str:
    c = COPY[lang]["home"]
    title = "".join(f'<span class="title-line">{escape(line)}</span>' for line in c["h1_lines"])
    benefits = "".join(f'<article class="benefit"><span aria-hidden="true">✓</span><h2>{escape(t)}</h2><p>{escape(p)}</p></article>' for t, p in c["benefits"])
    process = "".join(f'<article class="step"><span>{n}</span><h3>{escape(t)}</h3><p>{escape(p)}</p></article>' for n, t, p in c["process"])
    return f'''<section class="hero"><div class="hero-copy"><p class="eyebrow">{escape(c['eyebrow'])}</p><h1>{title}</h1><p class="hero-lead">{escape(c['lead'])}</p><div class="actions"><a class="button" href="{href(lang,'contact')}">{escape(c['primary'])}</a><a class="text-link" href="{href(lang,'services')}">{escape(c['secondary'])} →</a></div></div><div class="hero-orbit" aria-hidden="true"><div class="globe-lines"></div><span class="electron-orbit electron-one"><span class="electron-runner"><span class="electron"></span></span></span><span class="electron-orbit electron-two"><span class="electron-runner"><span class="electron"></span></span></span><span class="electron-orbit electron-three"><span class="electron-runner"><span class="electron"></span></span></span></div></section>
<section class="promise"><div><p class="eyebrow">TerraHit LLC</p><h2>{escape(c['promise_title'])}</h2></div><p>{escape(c['promise'])}</p></section>
<section class="benefits-grid">{benefits}</section>
<section class="section process-section"><div class="section-heading"><p class="eyebrow">PROCESS</p><h2>{escape(c['process_title'])}</h2></div><div class="process-grid">{process}</div></section>
<section class="scope"><div><p class="eyebrow">ALGERIA ↔ EUROPE</p><h2>{escape(c['scope_title'])}</h2><p>{escape(c['scope'])}</p></div><div class="scope-mark" aria-hidden="true">DZ<br><span>↔</span><br>EU</div></section>
<section class="closing"><h2>{escape(c['closing_title'])}</h2><p>{escape(c['closing'])}</p><a class="button button-light" href="{href(lang,'contact')}">{escape(c['primary'])}</a></section>'''


def page_header(title: str, intro: str = "") -> str:
    return f'<section class="page-hero"><p class="eyebrow">TerraHit LLC</p><h1>{escape(title)}</h1>' + (f'<p>{escape(intro)}</p>' if intro else '') + '</section>'


def about_body(lang: str) -> str:
    c = COPY[lang]["about"]
    sections = "".join(f'<article><h2>{escape(t)}</h2><p>{escape(p)}</p></article>' for t, p in c["sections"])
    values = "".join(f'<article><h3>{escape(t)}</h3><p>{escape(p)}</p></article>' for t, p in c["values"])
    return page_header(c["h1"], c["intro"]) + f'<section class="section prose-grid">{sections}</section><section class="section values"><div class="section-heading"><h2>{escape(c["values_title"])}</h2></div><div class="values-grid">{values}</div></section>'


def services_body(lang: str) -> str:
    c = COPY[lang]["services"]
    cards = "".join(f'<article class="service-card"><h2>{escape(t)}</h2><p>{escape(p)}</p></article>' for t, p in c["cards"])
    return page_header(c["h1"], c["intro"]) + f'<section class="section services-grid">{cards}</section><section class="boundary"><h2>{escape(c["boundary_title"])}</h2><p>{escape(c["boundary"])}</p></section>'


def contact_body(lang: str) -> str:
    c = COPY[lang]["contact"]
    opts = "".join(f'<option value="{escape(v)}">{escape(label)}</option>' for v, label in c["options"])
    return page_header(c["h1"], c["intro"]) + f'''<section class="section contact-layout">
  <aside class="contact-card"><h2>{escape(c['info'])}</h2><dl><dt>Email</dt><dd><a href="mailto:contact@terrahitb2b.com">contact@terrahitb2b.com</a></dd><dt>{escape(c['hq'])}</dt><dd>Albuquerque, New Mexico<br>United States</dd><dt>{escape(c['operations'])}</dt><dd>{escape(c['operations_value'])}</dd></dl></aside>
  <form class="contact-form" action="https://usebasin.com/f/3b9ec06003b5" method="post" data-success-url="{href(lang,'thanks')}" data-sending-label="{escape(c['sending'])}" data-error-message="{escape(c['error'])}">
    <div class="form-row"><div class="field"><label for="full-name">{escape(c['name'])}</label><input id="full-name" name="full_name" type="text" autocomplete="name" required></div><div class="field"><label for="company">{escape(c['company'])}</label><input id="company" name="company" type="text" autocomplete="organization"></div></div>
    <div class="field"><label for="email">{escape(c['email'])}</label><input id="email" name="email" type="email" autocomplete="email" required></div>
    <div class="field"><label for="operation-type">{escape(c['type'])}</label><select id="operation-type" name="operation_type"><option value="">{escape(c['select'])}</option>{opts}</select></div>
    <div class="field"><label for="message">{escape(c['message'])}</label><textarea id="message" name="message" rows="7" aria-describedby="message-help" required></textarea><small id="message-help">{escape(c['message_help'])}</small></div>
    <input type="text" name="_gotcha" class="honeypot" tabindex="-1" autocomplete="off" aria-hidden="true">
    <button class="button" type="submit">{escape(c['submit'])}</button>
    <p class="form-status" role="status" aria-live="polite" hidden></p>
    <p class="form-privacy">{escape(c['privacy_note'])} <a href="{href(lang,'privacy')}">{escape(c['privacy_link'])}</a>.</p>
  </form>
</section>'''


def thanks_body(lang: str) -> str:
    c = COPY[lang]["thanks"]
    return f'''<section class="thank-you"><div class="thank-you-card"><div class="success-mark" aria-hidden="true">✓</div><p class="eyebrow">TerraHit LLC</p><h1>{escape(c['h1'])}</h1><p class="thank-you-intro">{escape(c['intro'])}</p><p>{escape(c['message'])}</p><div class="actions thank-you-actions"><a class="button" href="{href(lang,'home')}">{escape(c['home'])}</a><a class="text-link" href="{href(lang,'contact')}">{escape(c['contact'])}</a></div></div></section>'''


def long_body(lang: str, page: str) -> str:
    c = COPY[lang][page]
    blocks = "".join(f'<section><h2>{escape(t)}</h2><p>{p}</p></section>' for t, p in c["blocks"])
    return page_header(c["h1"]) + f'<article class="legal-copy">{blocks}<p class="updated">{escape(c["updated"])}</p></article>'


def write_page(lang: str, page: str, body: str) -> None:
    directory = ROOT / LANGS[lang]["prefix"].lstrip("/")
    directory.mkdir(parents=True, exist_ok=True)
    (directory / PAGES[page]).write_text(base_page(lang, page, body), encoding="utf-8")


def not_found_page() -> str:
    return '''<!doctype html>
<html lang="en" dir="ltr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Page not found — TerraHit LLC</title>
  <meta name="description" content="The requested page could not be found on the TerraHit LLC website.">
  <meta name="robots" content="noindex,follow">
  <meta name="theme-color" content="#0b2f63">
  <link rel="icon" href="/favicon.ico?v=6" sizes="any">
  <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png?v=6">
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NCA2NCI+CiAgPGNpcmNsZSBjeD0iMzIiIGN5PSIzMiIgcj0iMzAiIGZpbGw9IiMwYjJmNjMiLz4KICA8Y2lyY2xlIGN4PSIzMSIgY3k9IjMxIiByPSIxOSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjZmZmZmZmIiBzdHJva2Utd2lkdGg9IjMiLz4KICA8cGF0aCBkPSJNMTIgMzFoMzhNMzEgMTJ2MzhNMTcgMjFjOCA1IDIwIDUgMjggME0xNyA0MWM3LTQgMTctNSAyNS0yTTMxIDEyYy03IDYtMTAgMTMtMTAgMTlzMyAxNCAxMCAxOU0zMSAxMmM3IDYgMTAgMTMgMTAgMTkgMCAzLS43IDYtMiA5IiBmaWxsPSJub25lIiBzdHJva2U9IiNmZmZmZmYiIHN0cm9rZS13aWR0aD0iMi41IiBzdHJva2UtbGluZWNhcD0icm91bmQiLz4KICA8cGF0aCBkPSJNMzggNDhjMi0xMCA4LTE1IDE3LTE2LTEgMTAtNiAxNi0xNyAxNloiIGZpbGw9IiMwMGE2NWEiLz4KICA8cGF0aCBkPSJNNDAgNDZjNC00IDgtNyAxMy0xMSIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjZmZmZmZmIiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIvPgo8L3N2Zz4K">
  <link rel="apple-touch-icon" sizes="180x180" href="/favicon_512x512.png?v=6">
  <link rel="stylesheet" href="/assets/styles.css?v=11">
</head>
<body>
  <header class="site-header">
    <div class="nav-shell">
      <a class="brand" id="brand-home" href="/" aria-label="TerraHit — Home"><img src="/logo_terrahit.webp?v=1" alt="TerraHit LLC" width="188" height="106" decoding="async"></a>
      <div class="language-switcher" aria-label="Languages">
        <button type="button" data-error-language="en" aria-pressed="true">EN</button>
        <button type="button" data-error-language="fr" aria-pressed="false">FR</button>
        <button type="button" data-error-language="ar" aria-pressed="false">AR</button>
      </div>
    </div>
  </header>
  <main class="thank-you" id="main">
    <section class="thank-you-card" aria-labelledby="error-title">
      <div class="error-code" aria-hidden="true">404</div>
      <p class="eyebrow">TerraHit LLC</p>
      <h1 id="error-title">Page not found</h1>
      <p class="thank-you-intro" id="error-intro">This page does not exist or may have been moved.</p>
      <p class="error-message" id="error-message">Return to the homepage or contact us to continue your Algeria–Europe trade operation.</p>
      <div class="actions thank-you-actions">
        <a class="button" id="error-home" href="/">Return to the homepage</a>
        <a class="text-link" id="error-contact" href="/contact.html">Contact TerraHit</a>
      </div>
    </section>
  </main>
  <footer class="error-footer">© 2026 TerraHit LLC · contact@terrahitb2b.com</footer>
  <script>
    (function () {
      var copy = {
        en: {lang:'en', dir:'ltr', title:'Page not found — TerraHit LLC', h1:'Page not found', intro:'This page does not exist or may have been moved.', message:'Return to the homepage or contact us to continue your Algeria–Europe trade operation.', home:'Return to the homepage', contact:'Contact TerraHit', homeUrl:'/', contactUrl:'/contact.html', homeLabel:'TerraHit — Home'},
        fr: {lang:'fr', dir:'ltr', title:'Page introuvable — TerraHit LLC', h1:'Page introuvable', intro:'Cette page n’existe pas ou a peut-être été déplacée.', message:'Revenez à l’accueil ou contactez-nous pour poursuivre votre opération commerciale Algérie–Europe.', home:'Retour à l’accueil', contact:'Contacter TerraHit', homeUrl:'/fr/', contactUrl:'/fr/contact.html', homeLabel:'TerraHit — Accueil'},
        ar: {lang:'ar', dir:'rtl', title:'الصفحة غير موجودة — TerraHit LLC', h1:'الصفحة غير موجودة', intro:'هذه الصفحة غير موجودة أو ربما تم نقلها.', message:'يمكنك العودة إلى الصفحة الرئيسية أو التواصل معنا لمتابعة عمليتك التجارية بين الجزائر وأوروبا.', home:'العودة إلى الصفحة الرئيسية', contact:'التواصل مع TerraHit', homeUrl:'/ar/', contactUrl:'/ar/contact.html', homeLabel:'TerraHit — الصفحة الرئيسية'}
      };
      var path = window.location.pathname.toLowerCase();
      var pathLanguage = path.indexOf('/fr/') === 0 ? 'fr' : path.indexOf('/ar/') === 0 ? 'ar' : '';
      var browserLanguage = ((navigator.languages && navigator.languages[0]) || navigator.language || 'en').toLowerCase();
      var detected = browserLanguage.indexOf('fr') === 0 ? 'fr' : browserLanguage.indexOf('ar') === 0 ? 'ar' : 'en';
      var saved = '';
      try { saved = localStorage.getItem('terrahit-language') || ''; } catch (error) {}

      function applyLanguage(language, remember) {
        var selected = copy[language] || copy.en;
        document.documentElement.lang = selected.lang;
        document.documentElement.dir = selected.dir;
        document.title = selected.title;
        document.getElementById('error-title').textContent = selected.h1;
        document.getElementById('error-intro').textContent = selected.intro;
        document.getElementById('error-message').textContent = selected.message;
        document.getElementById('error-home').textContent = selected.home;
        document.getElementById('error-home').href = selected.homeUrl;
        document.getElementById('error-contact').textContent = selected.contact;
        document.getElementById('error-contact').href = selected.contactUrl;
        document.getElementById('brand-home').href = selected.homeUrl;
        document.getElementById('brand-home').setAttribute('aria-label', selected.homeLabel);
        document.querySelectorAll('[data-error-language]').forEach(function (button) {
          button.setAttribute('aria-pressed', button.getAttribute('data-error-language') === selected.lang ? 'true' : 'false');
        });
        if (remember) {
          try { localStorage.setItem('terrahit-language', selected.lang); } catch (error) {}
        }
      }

      document.querySelectorAll('[data-error-language]').forEach(function (button) {
        button.addEventListener('click', function () { applyLanguage(button.getAttribute('data-error-language'), true); });
      });
      applyLanguage(pathLanguage || saved || detected, false);
    })();
  </script>
</body>
</html>
'''


def main() -> None:
    for lang in LANGS:
        write_page(lang, "home", home_body(lang))
        write_page(lang, "about", about_body(lang))
        write_page(lang, "services", services_body(lang))
        write_page(lang, "contact", contact_body(lang))
        write_page(lang, "thanks", thanks_body(lang))
        write_page(lang, "legal", long_body(lang, "legal"))
        write_page(lang, "privacy", long_body(lang, "privacy"))

    (ROOT / "404.html").write_text(not_found_page(), encoding="utf-8")

    urls = [canonical(lang, page) for lang in LANGS for page in PAGES if page != "thanks"]
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f'  <url><loc>{u}</loc></url>\n' for u in urls) + '</urlset>\n'
    (ROOT / "sitemap.xml").write_text(sitemap, encoding="utf-8")


if __name__ == "__main__":
    main()
