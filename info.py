# FLASK_ENV = production   Options: development, production
# FLASK_DEBUG=1            Enable debug mode (useful for development)

page_information = {
    "home": {
        "title": "JPM and Sons | Expert General Contractor Services on Long Island",
        "meta_description": "JPM and Sons offers general contracting services throughout Long Island. Specializing in masonry, concrete, asphalt paving, paver sealing, pressure washing, and home improvement. Get a free estimate today!"
    },
    "about_us": {
        "title": "About Us | JPM and Sons | General Contracting Services on Long Island",
        "meta_description": "Learn about JPM and Sons, your trusted general contractor serving Long Island. Dedicated to quality and professionalism in every project."
    },
    "contact_us": {
        "title": "Contact Us | JPM and Sons | Contracting Services in Long Island",
        "meta_description": "Contact JPM and Sons for a free estimate on your next project. We proudly serve Long Island with expert general contracting services."
    },
    "financing": {
        "title": "********",
        "meta_description": "Explore financing options with JPM and Sons. Affordable solutions for your masonry, concrete, asphalt, and home improvement projects."
    },
    "gallery": {
        "title": "Gallery | JPM and Sons | Masonry, Paver Sealing, Concrete, Pressure Washing",
        "meta_description": "Browse our gallery to see completed projects by JPM and Sons. We showcase masonry, concrete, asphalt paving, and more."
    },
    "asphalt": {
        "title": "Asphalt on Long Island | Driveways, Installation, Borders, Walkways",
        "meta_description": "JPM and Sons provides expert asphalt paving services for residential and commercial properties in Long Island. Durable and professional results."
    },
    "concrete": {
        "title": "Concrete on Long Island | Driveways, Patios, Walkways, Foundations",
        "meta_description": "High-quality concrete services by JPM and Sons, including driveways, patios, and foundations. Serving Long Island with excellence."
    },
    "home_improvement": {
        "title": "Home Improvement on Long Island | Kitchens, Roofing, Siding, Windows, Decks",
        "meta_description": "Enhance your living spaces with JPM and Sons’ professional home improvement services. Transform your home with expert craftsmanship."
    },
    "masonry": {
        "title": "Masonry on Long Island | Bricklaying, Stone, Retaining Walls, Repairs",
        "meta_description": "Expert masonry services by JPM and Sons, including brick, stone, and concrete work. Durable and aesthetic solutions for your property."
    },
    "paver_sealing": {
        "title": "Paver Sealing on Long Island | Cleaning, Sealing, Color Enhancement",
        "meta_description": "Protect and enhance your pavers with JPM and Sons’ premium paver sealing services. Serving Long Island with care."
    },
    "pressure_washing": {
        "title": "Pressure-washing on Long Island | Residential, Commercial, Decks, Fences",
        "meta_description": "Professional pressure washing services by JPM and Sons for decks, driveways, and exteriors. Refresh your property today!"
    }
}



services = {
    "asphalt": {
    "id": 1,
    "name": "asphalt",
    "less_information": "We provide professional asphalt paving services for driveways, walkways, parking lots, and basketball courts. Our skilled team ensures a durable and long-lasting finish using high-quality materials and proper installation techniques. Contact us for a consultation.",
    "information": "At JPM and Sons, we specialize in professional asphalt paving services that enhance and protect your outdoor spaces. Contact us today to learn more and schedule a consultation.",
    "sub_services": [
        {
            "name": "Driveway Installation",
            "description": "Expertly crafted driveways using high-quality materials, ensuring durability and a polished appearance that enhances curb appeal.",
            "long_description": "Our expertly crafted driveways use high-quality materials and advanced techniques to ensure durability and a polished appearance. Trusted by hundreds of customers in your area, we deliver fast and reliable service while ensuring peace of mind with our licensed and insured team.",
            "benefits": [
                "Enhances curb appeal and property value.",
                "Professionally graded for long-lasting durability.",
                "Licensed and insured team for a stress-free experience."
            ],
            "features": [
                "Customizable Designs",
                "Weather-Resistant Materials",
                "Smooth and Polished Finish"
            ],
            "image_path": "/static/images-webp/asphalt/asphalt_driveway_installation.webp",
            "buttons": [
                {"label": "Request Estimate", "link": "/contact-us", "style": "btn-primary"},
                {"label": "Read Reviews", "link": "/reviews", "style": "btn-outline-success"}
            ]
        },
        {
            "name": "Commercial Asphalt Installation",
            "description": "Providing robust asphalt solutions tailored for parking lots, walkways, and other commercial spaces.",
            "long_description": "Our commercial asphalt installation focuses on durability and performance for high-traffic areas. Trusted by hundreds of businesses, we provide licensed and insured services tailored to your needs.",
            "benefits": [
                "Designed for heavy usage and traffic.",
                "Ensures proper drainage and long-lasting performance.",
                "Compliance with industry standards and local regulations."
            ],
            "features": [
                "High Load-Bearing Capacity",
                "Precision Grading for Drainage",
                "Scalable for Large Areas"
            ],
            "image_path": "/static/images-webp/asphalt/asphalt_commercial_installation.webp",
            "buttons": [
                {"label": "View Gallery", "link": "/gallery", "style": "btn-outline-success"},
                {"label": "Schedule Consultation", "link": "/contact-us", "style": "btn-primary"}
            ]
        },
        {
            "name": "Belgium Block Borders",
            "description": "Precision installation of decorative Belgium block borders to define the edges of your driveway or walkway.",
            "long_description": "Our decorative Belgium block borders combine elegance with functionality, ensuring structural integrity and a finished look. Fully licensed and trusted by customers, we provide reliable service tailored to your project's needs.",
            "benefits": [
                "Prevents erosion and edge deterioration.",
                "Adds an elegant and finished look to your space.",
                "Durable and weather-resistant installation."
            ],
            "features": [
                "Decorative and Functional",
                "High-Quality Belgium Blocks",
                "Customizable for Any Project"
            ],
            "image_path": "/static/images-webp/asphalt/asphalt_belgium_block_borders.webp",
            "buttons": [
                {"label": "Get a Quote", "link": "/contact-us", "style": "btn-primary"},
                {"label": "View our work", "link": "/gallery", "style": "btn-outline-success"}
            ]
        },
        {
            "name": "Paver Walkways",
            "description": "Design and installation of beautiful paver walkways that combine aesthetics with functionality.",
            "long_description": "We specialize in the design and installation of stunning paver walkways that elevate the beauty and functionality of your property. Using high-quality materials and precise techniques, we ensure your walkways are durable, slip-resistant, and visually appealing. Trusted by customers in your area, our licensed and insured team guarantees reliable service tailored to your needs.",
            "benefits": [
                "Improves property accessibility and visual appeal.",
                "Slip-resistant for enhanced safety.",
                "Long-lasting and easy to maintain."
            ],
            "features": [
                "Slip-Resistant Materials",
                "Enhanced Accessibility",
                "Customizable Designs"
            ],
            "image_path": "/static/images-webp/asphalt/asphalt_paver_walkways.webp",
            "buttons": [
                {"label": "Request a Free Quote", "link": "contact-us", "style": "btn-primary"},
                {"label": "View Portfolio", "link": "/gallery", "style": "btn-outline-success"}
            ]
        }
    ]
},


"concrete": {
    "id": 2,
    "name": "concrete",
    "less_information": "Our concrete services include driveways, patios, sidewalks, and steps. We focus on quality and precision, ensuring long-lasting results for all installations. Whether it's a decorative patio or a functional driveway, we deliver exceptional craftsmanship.",
    "information": "At JPM and Sons, we specialize in professional concrete services that enhance and protect your outdoor and indoor spaces. Contact us today to learn more about our services and schedule a consultation.",
    "sub_services": [
        {
            "name": "Driveway Installation",
            "description": "Expert installation of durable and smooth concrete driveways.",
            "long_description": "Our concrete driveway installations are designed for strength and elegance, incorporating proper grading, reinforcement, and finishing techniques. Trusted by hundreds of customers, we ensure fully licensed and insured service, delivering fast and reliable results tailored to your needs.",
            "benefits": [
                "Enhances curb appeal and increases property value.",
                "Designed to withstand heavy vehicles and usage.",
                "Precision installation with proper grading for longevity."
            ],
            "features": [
                "Reinforced for Heavy Loads",
                "Weather-Resistant Finish",
                "Seamless, Polished Look"
            ],
            "image_path": "/static/images-webp/concrete/concrete_driveway_installation.webp",
            "buttons": [
                {"label": "Request Estimate", "link": "/contact-us", "style": "btn-outline-primary"},
                {"label": "View Portfolio", "link": "/gallery", "style": "btn-secondary"}
            ]
        },
        {
            "name": "Patios and Walkways",
            "description": "Design and installation of beautiful and functional concrete patios and walkways.",
            "long_description": "Our patios and walkways seamlessly blend with your landscaping, creating stunning and durable outdoor living spaces. Fully licensed and trusted by customers, we prioritize high-quality craftsmanship and efficient service.",
            "benefits": [
                "Improves outdoor functionality and aesthetic appeal.",
                "Durable and weather-resistant for all seasons.",
                "Low maintenance and long-lasting materials."
            ],
            "features": [
                "Custom Designs for Your Space",
                "Slip-Resistant Surface",
                "Seamlessly Integrated with Landscaping"
            ],
            "image_path": "/static/images-webp/concrete/concrete_patios.webp",
            "buttons": [
                {"label": "Get a Quote", "link": "/estimate/2", "style": "btn-outline-dark"},
                {"label": "Schedule Consultation", "link": "/contact", "style": "btn-danger"}
            ]
        },
        {
            "name": "Sidewalks and Aprons",
            "description": "Professional installation of sidewalks and aprons, ensuring safe and attractive transitions from street to driveway.",
            "long_description": "From residential sidewalks to driveway aprons, we ensure smooth, durable, and visually appealing transitions. Our fully licensed and insured team delivers trusted and reliable service tailored to your specific needs.",
            "benefits": [
                "Improves safety with smooth, even surfaces.",
                "Designed to handle pedestrian and vehicular traffic.",
                "Compliance with local codes and regulations."
            ],
            "features": [
                "Slip-Resistant Surfaces",
                "Durable Concrete Construction",
                "Integrated Drainage Solutions"
            ],
            "image_path": "/static/images-webp/concrete/concrete_walkway.webp",
            "buttons": [
                {"label": "Contact Us", "link": "/contact", "style": "btn-primary"},
                {"label": "Read Reviews", "link": "/reviews", "style": "btn-success"}
            ]
        },
        {
            "name": "Steps, Stoops, and Foundation",
            "description": "Create safe and attractive entryways with our expertly installed steps, stoops, and foundations.",
            "long_description": "Our expert team specializes in constructing sturdy and aesthetically pleasing steps, stoops, and foundations. Trusted by hundreds, we provide licensed and reliable service to ensure high-quality results.",
            "benefits": [
                "Adds structural stability and curb appeal.",
                "Designed to meet your home's unique style and needs.",
                "Built for durability and safety in high-traffic areas."
            ],
            "features": [
                "Reinforced for Durability",
                "Customizable Designs",
                "Weather-Resistant Materials"
            ],
            "image_path": "/static/images-webp/concrete/concrete_stoops.webp",
            "buttons": [
                {"label": "View Portfolio", "link": "/gallery", "style": "btn-outline-primary"},
                {"label": "Request a Free Estimate", "link": "/estimate/2", "style": "btn-danger"}
            ]
        }
    ]
},
 
"home_improvement": {
    "id": 3,
    "name": "home improvement",
    "less_information": "From kitchen remodeling to bathroom renovations, our home improvement services enhance the beauty and functionality of your home. We specialize in siding, roofing, and flooring installations, delivering quality results tailored to your needs.",
    "information": "At JPM and Sons, we offer specialized home improvement services dedicated to enhancing the beauty, functionality, and value of your property. Whether you're planning a kitchen remodel, bathroom renovation, or any other home improvement project, our experienced team is ready to assist you.",
    "sub_services": [
        {
            "name": "Kitchen Remodeling",
            "description": "Transform your kitchen into a modern, functional space.",
            "long_description": "Our expert kitchen remodeling services include custom cabinetry, countertops, flooring, lighting, and appliance installation. We focus on creating a kitchen that balances beauty and efficiency, tailored to your lifestyle.",
            "benefits": [
                "Enhances cooking and dining experience.",
                "Increases home value significantly.",
                "Optimizes space for better functionality."
            ],
            "features": [
                "Custom Cabinetry",
                "Energy-Efficient Appliances",
                "Modern Lighting Solutions"
            ],
            "image_path": "/static/images-webp/home_improvement/home_improvement_kitchen_remodel.webp",
            "buttons": [
                {"label": "Get a Free Quote", "link": "/estimate/3", "style": "btn-outline-primary"},
                {"label": "View Portfolio", "link": "/gallery", "style": "btn-secondary"}
            ]
        },
        {
            "name": "Bathroom Renovation",
            "description": "Upgrade your bathroom into a luxurious retreat.",
            "long_description": "Our bathroom renovations include tile work, custom vanities, modern fixtures, and lighting to create a bathroom that combines comfort and elegance. We ensure high-quality craftsmanship tailored to your needs.",
            "benefits": [
                "Improves comfort and relaxation.",
                "Enhances aesthetic appeal.",
                "Boosts property resale value."
            ],
            "features": [
                "Spa-Inspired Designs",
                "Water-Saving Fixtures",
                "Heated Flooring Options"
            ],
            "image_path": "/static/images-webp/home_improvement/home_improvement_bathroom_renovation.webp",
            "buttons": [
                {"label": "Schedule Consultation", "link": "/contact", "style": "btn-danger"},
                {"label": "Read Reviews", "link": "/reviews", "style": "btn-success"}
            ]
        },
        {
            "name": "Roofing Services",
            "description": "Protect your home with durable, high-quality roofing solutions.",
            "long_description": "Our roofing services include installation, repair, and maintenance to ensure your home remains secure and weatherproof. We provide trusted and reliable service tailored to your roofing needs.",
            "benefits": [
                "Ensures structural integrity.",
                "Prevents leaks and water damage.",
                "Improves energy efficiency."
            ],
            "features": [
                "High-Quality Materials",
                "Weather-Resistant Construction",
                "Comprehensive Warranty"
            ],
            "image_path": "/static/images-webp/home_improvement/home_improvement_roofing.webp",
            "buttons": [
                {"label": "Contact Us", "link": "/contact", "style": "btn-primary"},
                {"label": "Request Estimate", "link": "/contact-us", "style": "btn-outline-dark"}
            ]
        },
        {
            "name": "Siding Installation",
            "description": "Enhance your home's exterior with premium siding solutions.",
            "long_description": "We offer a variety of siding materials, such as vinyl, fiber cement, and wood, to improve your home's curb appeal and energy efficiency. Our services transform your home's exterior with quality and style.",
            "benefits": [
                "Increases curb appeal.",
                "Provides additional insulation.",
                "Low maintenance and durable."
            ],
            "features": [
                "Variety of Material Options",
                "Fade-Resistant Colors",
                "Professional Installation"
            ],
            "image_path": "/static/images-webp/home_improvement/home_improvement_siding.webp",
            "buttons": [
                {"label": "Schedule Consultation", "link": "/contact", "style": "btn-danger"},
                {"label": "View Our Work", "link": "/gallery", "style": "btn-outline-primary"}
            ]
        },
        {
            "name": "Window Replacement",
            "description": "Improve energy efficiency and aesthetics with new windows.",
            "long_description": "Our window replacement services include custom-sized windows with modern styles and high-performance glass for better insulation and style. We deliver reliable and high-quality results to enhance your home's comfort.",
            "benefits": [
                "Reduces energy costs.",
                "Enhances natural light.",
                "Improves home security."
            ],
            "features": [
                "Energy-Efficient Glass",
                "Customizable Designs",
                "Secure Locking Mechanisms"
            ],
            "image_path": "/static/images-webp/home_improvement/home_improvement_window_installation.webp",
            "buttons": [
                {"label": "Contact Us", "link": "/contact", "style": "btn-primary"},
                {"label": "Request a Quote", "link": "/estimate/3", "style": "btn-outline-dark"}
            ]
        },
        {
            "name": "Flooring Installation",
            "description": "Upgrade your interior with professional flooring installation.",
            "long_description": "From hardwood to tile and luxury vinyl, our flooring services offer quality materials and expert installation for a seamless finish. We provide licensed and reliable service tailored to your needs.",
            "benefits": [
                "Enhances interior aesthetics.",
                "Increases property value.",
                "Provides durable and easy-to-clean surfaces."
            ],
            "features": [
                "Wide Range of Materials",
                "Precision Installation",
                "Scratch and Stain Resistant Options"
            ],
            "image_path": "/static/images-webp/home_improvement/home_improvement_flooring_installation.webp",
            "buttons": [
                {"label": "View Portfolio", "link": "/gallery", "style": "btn-outline-primary"},
                {"label": "Schedule Consultation", "link": "/contact", "style": "btn-danger"}
            ]
        }
    ]
},

"masonry": {
    "id": 4,
    "name": "masonry",
    "less_information": "Our masonry services feature custom brickwork, retaining walls, and outdoor barbecues. We combine durability with aesthetic appeal to create functional and beautiful structures, tailored to your property's unique design.",
    "information": "At JPM and Sons, we offer a variety of masonry services to help you build and maintain your property. Whether you need a new patio, a stone retaining wall, or repairs to your existing masonry, we take pride in delivering exceptional results tailored to your needs.",
    "sub_services": [
        {
            "name": "Custom Brickwork and Paver Installation",
            "description": "Enhance your property with durable and stylish brickwork.",
            "long_description": "Our custom brickwork and paver installations are perfect for patios, walkways, and driveways. We blend durability with aesthetic appeal to create a polished and functional finish. Trusted by hundreds of customers, our licensed and insured team ensures reliable and efficient service.",
            "benefits": [
                "Design versatility for personalized outdoor spaces.",
                "Durable and crack-resistant construction.",
                "Minimal maintenance for long-term cost savings."
            ],
            "features": [
                "Wide Range of Design Options",
                "Weather-Resistant Materials",
                "Polished and Seamless Finish"
            ],
            "image_path": "/static/images-webp/masonry/masonry_custom_brickwork.webp",
            "buttons": [
                {"label": "View Portfolio", "link": "/gallery", "style": "btn-outline-primary"},
                {"label": "Request a Quote", "link": "/estimate/4", "style": "btn-danger"}
            ]
        },
        {
            "name": "Stone Veneer and Cultured Stone",
            "description": "Add elegance with stone veneers and cultured stone.",
            "long_description": "Our stone veneer and cultured stone installations are ideal for walls, fireplaces, and exterior facades. We ensure a sophisticated, natural look that enhances the elegance of your property. Licensed and insured, our team provides trusted service tailored to your needs.",
            "benefits": [
                "Provides a sophisticated and authentic look.",
                "Cost-effective alternative to natural stone.",
                "Lightweight and easy to install."
            ],
            "features": [
                "Authentic and Elegant Design",
                "Wide Variety of Styles",
                "Increased Property Value"
            ],
            "image_path": "/static/images-webp/masonry/masonry_stone_veneers.webp",
            "buttons": [
                {"label": "Contact Us", "link": "/contact", "style": "btn-primary"},
                {"label": "Read Reviews", "link": "/reviews", "style": "btn-success"}
            ]
        },
        {
            "name": "Outdoor Barbecues",
            "description": "Create the ultimate backyard entertaining space.",
            "long_description": "We design and build custom outdoor barbecue areas, complete with stone or brick surrounds. These spaces are perfect for entertaining and enhancing the functionality of your outdoor living area. Trusted and licensed, we deliver exceptional craftsmanship.",
            "benefits": [
                "Creates a functional and stylish entertaining area.",
                "Boosts outdoor living appeal and usability.",
                "Adds long-term value to your property."
            ],
            "features": [
                "Custom Designs to Suit Your Needs",
                "Durable and Weather-Resistant Materials",
                "Expert Craftsmanship for a Polished Look"
            ],
            "image_path": "/static/images-webp/masonry/masonry_outdoor_barbecues.webp",
            "buttons": [
                {"label": "Get a Free Quote", "link": "/estimate/4", "style": "btn-outline-dark"},
                {"label": "View Our Work", "link": "/gallery", "style": "btn-outline-secondary"}
            ]
        },
        {
            "name": "Retaining Walls and Stoops",
            "description": "Build functional and decorative retaining walls and stoops.",
            "long_description": "Our retaining walls and stoops are designed to provide structural stability while complementing your landscaping. Licensed and trusted by customers, we ensure durable and visually appealing results.",
            "benefits": [
                "Prevents soil erosion and water runoff.",
                "Enhances the structural integrity of your landscape.",
                "Adds aesthetic value to outdoor spaces."
            ],
            "features": [
                "Structural Stability",
                "Customizable Designs for Any Space",
                "Low Maintenance and Long-Lasting"
            ],
            "image_path": "/static/images-webp/masonry/masonry_retaining_walls.webp",
            "buttons": [
                {"label": "Request Estimate", "link": "/contact-us", "style": "btn-outline-primary"},
                {"label": "Schedule Consultation", "link": "/contact", "style": "btn-danger"}
            ]
        }
    ]
},

"paver_sealing": {
    "id": 5,
    "name": "paver sealing",
    "less_information": "Revitalize and protect your outdoor spaces with our paver sealing services. We offer thorough cleaning, polymeric sand application, and high-grade sealing to enhance the look and durability of your pavers.",
    "information": "We specialize in professional paver sealing services that protect and enhance your outdoor spaces. Our skilled team can revitalize your paver patios, walkways, and driveways using high-grade sealants sourced directly from our trusted supplier. With over 35 years of experience, we deliver results that last.",
    "sub_services": [
        {
            "name": "Hot Water Pressure Washing",
            "description": "Clean pavers with hot water for a fresh start.",
            "long_description": "Our hot water pressure washing removes dirt, debris, and stains from your pavers, preparing them for a flawless sealing application. Trusted by hundreds, we provide fast and reliable service backed by our licensed and insured team.",
            "benefits": [
                "Effectively removes stubborn dirt and stains.",
                "Prepares pavers for optimal sealing results.",
                "Eco-friendly cleaning process using hot water."
            ],
            "features": [
                "High-Pressure Cleaning Technology",
                "Eco-Friendly and Safe Methods",
                "Quick and Thorough Cleaning"
            ],
            "image_path": "/static/images-webp/paver_sealing/paver_sealing_hot_water_washing.webp",
            "buttons": [
                {"label": "Request a Quote", "link": "/estimate/5", "style": "btn-outline-primary"},
                {"label": "Contact Us", "link": "/contact", "style": "btn-danger"}
            ]
        },
        {
            "name": "Polymeric Sand Application",
            "description": "Seal joints with durable polymeric sand.",
            "long_description": "We use premium polymeric sand to fill paver joints, preventing weed growth and ensuring a stable, interlocked surface. Trusted by hundreds, our licensed team ensures long-lasting results tailored to your needs.",
            "benefits": [
                "Prevents weed and grass growth between pavers.",
                "Provides a stable, interlocked surface.",
                "Reduces erosion and water damage."
            ],
            "features": [
                "High-Quality Polymeric Sand",
                "Weed Prevention and Stability",
                "Long-Lasting Joint Sealing"
            ],
            "image_path": "/static/images-webp/paver_sealing/paver_sealing_sand_application.webp",
            "buttons": [
                {"label": "Schedule Consultation", "link": "/contact", "style": "btn-danger"},
                {"label": "Read Reviews", "link": "/reviews", "style": "btn-success"}
            ]
        },
        {
            "name": "Sealing Application",
            "description": "Apply premium sealants for protection and shine.",
            "long_description": "Our high-quality sealants protect pavers from stains, weather damage, and fading while enhancing their natural color and texture. With over 35 years of experience, we ensure reliable and professional service every time.",
            "benefits": [
                "Protects pavers from stains and fading.",
                "Enhances the natural color and texture of pavers.",
                "Increases resistance to weather damage."
            ],
            "features": [
                "Premium Sealants for Long-Lasting Protection",
                "Weatherproof and UV-Resistant Coating",
                "Enhances Color and Texture"
            ],
            "image_path": "/static/images-webp/paver_sealing/paver_sealing_sealing_application.webp",
            "buttons": [
                {"label": "View Portfolio", "link": "/gallery", "style": "btn-outline-secondary"},
                {"label": "Request a Free Quote", "link": "/estimate/5", "style": "btn-outline-dark"}
            ]
        },
        {
            "name": "Paver Repair",
            "description": "Fix damaged or sunken pavers.",
            "long_description": "Our paver repair services address cracks, shifting, and uneven surfaces, restoring the safety and beauty of your outdoor spaces. Trusted by customers, we deliver reliable and efficient repairs tailored to your needs.",
            "benefits": [
                "Restores safety by leveling uneven surfaces.",
                "Improves the visual appeal of damaged pavers.",
                "Extends the lifespan of your paver installation."
            ],
            "features": [
                "Precision Repair for Cracks and Shifts",
                "Stability and Safety Improvements",
                "Seamless Restoration of Appearance"
            ],
            "image_path": "/static/images-webp/paver_sealing/paver_sealing_paver_repair.webp",
            "buttons": [
                {"label": "Contact Us", "link": "/contact", "style": "btn-primary"},
                {"label": "Schedule Service", "link": "/estimate/5", "style": "btn-danger"}
            ]
        }
    ]
},

"pressure_washing": {
    "id": 6,
    "name": "pressure washing",
    "less_information": "Our pressure washing services clean and restore decks, driveways, patios, and building exteriors. Using professional-grade equipment, we remove dirt, stains, and mildew to maintain your property's beauty and value.",
    "information": "Our pressure washing services ensure your property stays clean and well-maintained. Whether it's your home's exterior, deck, driveway, or patio, our skilled team uses high-quality equipment and specialized techniques to clean safely and effectively.",
    "sub_services": [
        {
            "name": "Residential Pressure Washing",
            "description": "Clean your home's exterior with ease.",
            "long_description": "We specialize in cleaning decks, driveways, patios, and siding, removing dirt, mildew, and stains for a refreshed appearance. Trusted by hundreds of customers, we provide licensed and insured service that is fast and reliable.",
            "benefits": [
                "Removes dirt, mold, and mildew effectively.",
                "Improves your home's curb appeal.",
                "Protects surfaces from long-term damage."
            ],
            "features": [
                "High-Pressure Cleaning Equipment",
                "Eco-Friendly Cleaning Solutions",
                "Fast and Thorough Service"
            ],
            "image_path": "/static/images-webp/pressure_washing/pressure_washing_residential.webp",
            "buttons": [
                {"label": "Request a Free Quote", "link": "/estimate/6", "style": "btn-outline-primary"},
                {"label": "Read Reviews", "link": "/reviews", "style": "btn-success"}
            ]
        },
        {
            "name": "Commercial Pressure Washing",
            "description": "Restore your business’s exterior surfaces.",
            "long_description": "Our commercial pressure washing services ensure your property is clean and inviting, removing grime from parking lots, storefronts, and sidewalks. We deliver trusted, licensed, and insured service for long-lasting results.",
            "benefits": [
                "Enhances the professional appearance of your property.",
                "Eliminates tough stains and grime from high-traffic areas.",
                "Helps extend the lifespan of outdoor surfaces."
            ],
            "features": [
                "Industrial-Grade Cleaning Equipment",
                "Tailored Solutions for Businesses",
                "Improves Safety and Cleanliness"
            ],
            "image_path": "/static/images-webp/pressure_washing/pressure_washing_commercial.webp",
            "buttons": [
                {"label": "Schedule Consultation", "link": "/contact", "style": "btn-danger"},
                {"label": "View Portfolio", "link": "/gallery", "style": "btn-outline-secondary"}
            ]
        },
        {
            "name": "Surface Preparation",
            "description": "Prepare surfaces for painting or sealing.",
            "long_description": "We clean and prepare surfaces by removing dirt, old paint, and debris, ensuring proper adhesion for new finishes. Trusted by customers, we offer licensed and reliable service to guarantee excellent results.",
            "benefits": [
                "Removes debris and old finishes efficiently.",
                "Improves adhesion for painting or sealing.",
                "Ensures a smooth, professional final result."
            ],
            "features": [
                "High-Precision Cleaning Techniques",
                "Safe for All Surfaces",
                "Prepares for Long-Lasting Coatings"
            ],
            "image_path": "/static/images-webp/pressure_washing/pressure_washing_surface_preparation.webp",
            "buttons": [
                {"label": "Contact Us", "link": "/contact-us", "style": "btn-primary"},
                {"label": "Request Estimate", "link": "/estimate/6", "style": "btn-outline-dark"}
            ]
        },
        {
            "name": "Deck and Fence Cleaning",
            "description": "Revitalize your wooden decks and fences.",
            "long_description": "Our gentle cleaning techniques remove dirt and mildew from wood, restoring its natural beauty and preserving its longevity. Trusted by hundreds, we ensure reliable, licensed, and professional service for lasting results.",
            "benefits": [
                "Restores the natural beauty of wood surfaces.",
                "Prevents rot and decay caused by mildew.",
                "Prolongs the life of your deck or fence."
            ],
            "features": [
                "Gentle, Non-Damaging Cleaning Techniques",
                "Preserves Wood Integrity",
                "Eco-Friendly Cleaning Options"
            ],
            "image_path": "/static/images-webp/pressure_washing/pressure_washing_deck.webp",
            "buttons": [
                {"label": "Request a Quote", "link": "/estimate/6", "style": "btn-outline-primary"},
                {"label": "Read Reviews", "link": "/reviews", "style": "btn-success"}
            ]
        }
    ]
}




}


gallery_and_alt = [
    {"file": "backyard-patio.webp", "alt": "A beautifully designed backyard patio with outdoor furniture.", "stackable": True},
    {"file": "backyard-patio-pavers.webp", "alt": "Backyard area with freshly sealed decorative pavers."},
    {"file": "backyard-pavers.webp", "alt": "Backyard area with freshly sealed decorative pavers."},
    {"file": "backyard-pool.webp", "alt": "A backyard pool with clear blue water and a relaxing deck."},
    {"file": "bathroom-modern.webp", "alt": "A modern bathroom with sleek fixtures and a large mirror.", "stackable": True},
    {"file": "bathtub-white.webp", "alt": "An elegant white freestanding bathtub with a stylish faucet.", "stackable": True},
    {"file": "driveway-sealed.webp", "alt": "A driveway freshly sealed and protected for longevity."},
    {"file": "driveway-sparkling.webp", "alt": "A sparkling clean driveway after thorough washing."},
    {"file": "fire-pit-backyard.webp", "alt": "A cozy backyard fire pit surrounded by seating."},
    {"file": "front-steps.webp", "alt": "Newly renovated front steps leading to the entrance.", "stackable": True},
    {"file": "front-yard-patio.webp", "alt": "A stylish front yard patio with decorative pavers."},
    {"file": "full-view-kitchen.webp", "alt": "A full view of a spacious modern kitchen with high-end appliances.", "stackable": True},
    {"file": "full-view-living-room.webp", "alt": "A spacious living room with modern furniture and decor.", "stackable": True},
    {"file": "kitchen-modern.webp", "alt": "A modern kitchen with updated appliances and sleek countertops.", "stackable": True},
    {"file": "kitchen-wood-floors.webp", "alt": "A kitchen featuring polished wooden floors and bright lighting.", "stackable": True},
    {"file": "living-room-design.webp", "alt": "A cozy and stylish living room with elegant furniture.", "stackable": True},
    {"file": "living-room-interior.webp", "alt": "The interior of a modern living room with large windows.", "stackable": True},
    {"file": "living-room-modern.webp", "alt": "A contemporary living room with modern decor and a comfortable setup.", "stackable": True},
    {"file": "marble-counters.webp", "alt": "Luxurious marble countertops in a spacious kitchen.", "stackable": True},
    {"file": "new-stairs-modern.webp", "alt": "Modern wooden stairs with a sleek design and polished finish.", "stackable": True},
    {"file": "outdoor-bbq.webp", "alt": "An outdoor BBQ area with a grill and seating for gatherings.", "stackable": True},
    {"file": "overlooking-water-view.webp", "alt": "A scenic view overlooking calm water during sunset.", "stackable": True},
    {"file": "pavers-sealed.webp", "alt": "Freshly sealed pavers on a backyard patio."},
    {"file": "pool-backyard.webp", "alt": "A beautiful backyard pool surrounded by a relaxing deck."},
    {"file": "stairs-wooden-floors.webp", "alt": "Wooden stairs with polished floors leading to the next level.", "stackable": True},
    {"file": "walkway-front-yard.webp", "alt": "A front yard walkway made with decorative pavers."},
    {"file": "walkway-garden.webp", "alt": "A garden walkway surrounded by vibrant flowers."},
    {"file": "walkway-side.webp", "alt": "A side walkway leading to the backyard of a house."},
    {"file": "windows-large.webp", "alt": "Large windows with a clear view of the outdoor landscape.", "stackable": True}
]

  
before_afters = [
    {
        "before": {"file": "before-washing-and-sealant.webp", "alt": "Before washing and sealant: dirt and grime on surface"},
        "after": {"file": "after-washing-and-sealant.webp", "alt": "After washing and sealant: sparkling clean and vibrant surface"}
    },
    {
        "before": {"file": "before-washing-and-sealant-2.webp", "alt": "Before washing and sealant: faded and stained concrete"},
        "after": {"file": "after-washing-and-sealant-2.webp", "alt": "After washing and sealant: refreshed and sealed concrete"}
    },
    {
        "before": {"file": "before-washing-and-sealant-3.webp", "alt": "Before washing and sealant: driveway with visible wear"},
        "after": {"file": "after-washing-and-sealant-3.webp", "alt": "After washing and sealant: driveway restored to like-new condition"}
    },
    {
        "before": {"file": "before-washing-and-sealant-4.webp", "alt": "Before washing and sealant: patio with grime buildup"},
        "after": {"file": "after-washing-and-sealant-4.webp", "alt": "After washing and sealant: patio looking spotless and vibrant"}
    },
    {
        "before": {"file": "before-paver-repair-and-restoration.webp", "alt": "Before paver repair and restoration: uneven and damaged pavers"},
        "after": {"file": "after-paver-repair-and-restoration.webp", "alt": "After paver repair and restoration: perfectly aligned and restored pavers"}
    },
    {
        "before": {"file": "before-washing-and-sealant-5.webp", "alt": "Before washing and sealant: walkway with heavy dirt stains"},
        "after": {"file": "after-washing-and-sealant-5.webp", "alt": "After washing and sealant: walkway restored and sealed"}
    },
    {
        "before": {"file": "before-washing-and-restoration.webp", "alt": "Before washing and restoration: neglected backyard area"},
        "after": {"file": "after-washing-and-restoration.webp", "alt": "After washing and restoration: beautifully restored backyard area"}
    },
    {
        "before": {"file": "before-pavers-sealant.webp", "alt": "Before pavers sealant: dull and unprotected pavers"},
        "after": {"file": "after-pavers-sealant.webp", "alt": "After pavers sealant: pavers with a glossy and protected finish"}
    },
    {
        "before": {"file": "before-pavers-sealant-2.webp", "alt": "Before pavers sealant: discolored and unsealed pavers"},
        "after": {"file": "after-pavers-sealant-2.webp", "alt": "After pavers sealant: vibrant and well-protected pavers"}
    },
    {
        "before": {"file": "before-and-after-sealant.webp", "alt": "Side-by-side comparison of before and after sealant application"},
        "after": {"file": "before-and-after-sealant.webp", "alt": "Side-by-side comparison of before and after sealant application"}
    }
]




