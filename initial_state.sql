UPDATE django_site SET DOMAIN = 'localhost:8000', `name` = 'Facebook' WHERE id=1;
INSERT INTO socialaccount_socialapp (provider, `name`, secret, client_id, `key`)
VALUES ("facebook", "Facebook", "facebook_app_secret", "facebook_app_id", '');
INSERT INTO socialaccount_socialapp_sites (socialapp_id, site_id) VALUES (1,1);
