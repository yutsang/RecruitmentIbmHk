Select owner.owner_id, owner.owner_name, count(distinct category.category_id) from owner
    join article on owner.owner_id = article.article_id
    join category_aricle_mapping on article.article_id = category_aricle_mapping.category_id
    join category on category.category_id = category_aricle_mapping.category_id