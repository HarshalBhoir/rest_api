{
    "name": "Odoo Rest API",
    "version": "1.0.1",
    "category": "API",
    "author": "Jamshid K",
    "website": "jamshu.github.io",
    "summary": "Odoo Rest API",
    "support": "jamshu.mkd@gmail.com",
    "description": """ Rest API For Odoo  
    
    data obj can be create update delete throgh this api
    api with access token""",
    "depends": ["web"],
    "data": ["data/ir_config_param.xml", "views/ir_model.xml", "views/res_users.xml", "security/ir.model.access.csv",],
  
   
    "installable": True,
    "auto_install": False,
}
