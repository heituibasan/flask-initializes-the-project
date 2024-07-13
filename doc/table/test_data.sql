-- 用户表测试数据
INSERT INTO users (username, email, password, code, phone, qq, role, create_time, last_login_time, create_mac,
                   create_ip, last_login_ip, address, city, status)
VALUES ('Alice', 'alice@example.com', 'hashed_password', 'verification_code_123', 1234567890, '123456789', '0', NOW(),
        NOW(), 'AA:BB:CC:DD:EE', '192.168.1.100', '192.168.1.100', '123 Main St', 'New York', 1),
       ('Bob', 'bob@example.com', 'hashed_password', 'verification_code_456', 9876543210, '987654321', '1', NOW(),
        NOW(), 'FF:GG:HH:II:JJ', '192.168.1.101', '192.168.1.101', '456 Elm St', 'Los Angeles', 1);

-- 文章表测试数据
INSERT INTO articles (author_id, cover, label, sort, content, password, status, like_num, comment_num, files,
                      create_time, release_time, update_time, create_ip)
VALUES ('author1', 'https://example.com/cover.jpg', '1,2', '3,4',
        'This is the content of the article in Markdown format.', NULL, 0, 0, 0, '[
    1,
    2,
    3
  ]', NOW(), NOW(), NOW(), '192.168.1.102'),
       ('author2', 'https://example.com/cover2.jpg', '3,4', '5,6', 'Another article content in Markdown.', NULL, 0, 0,
        0, '[
         4,
         5,
         6
       ]', NOW(), NOW(), NOW(), '192.168.1.103');

-- 分类表测试数据
INSERT INTO categories (content, author_id, status, create_time)
VALUES ('Technology', 'author1', 0, NOW()),
       ('Travel', 'author2', 0, NOW());

-- 标签表测试数据
INSERT INTO tags (content, author_id, status, create_time)
VALUES ('Programming', 'author1', 0, NOW()),
       ('Nature', 'author2', 0, NOW());

-- 评论表测试数据
INSERT INTO comments (author_id, article_id, title, content, like_num, comment_num, create_time, create_ip, status,
                      auditing_status, father_id)
VALUES ('user1', 'article1', 'Comment Title 1', 'This is a comment on article 1.', 0, 0, NOW(), '192.168.1.104', 0, 1,
        NULL),
       ('user2', 'article2', 'Comment Title 2', 'Another comment on article 2.', 0, 0, NOW(), '192.168.1.105', 0, 1,
        NULL);

-- 附件表测试数据
INSERT INTO attachments (author_id, network_url, local_url, preview_url, size, status, create_time, create_ip)
VALUES ('author1', 'https://example.com/file1.pdf', '/var/www/files/file1.pdf', 'https://example.com/preview/file1.pdf',
        1024, 0, NOW(), '192.168.1.106'),
       ('author2', 'https://example.com/file2.docx', '/var/www/files/file2.docx',
        'https://example.com/preview/file2.docx', 2048, 0, NOW(), '192.168.1.107');

-- 链接表测试数据
INSERT INTO links (title, content, author_id, status, create_time)
VALUES ('Useful Link 1', 'https://example.com/link1', 'author1', 0, NOW()),
       ('Helpful Link 2', 'https://example.com/link2', 'author2', 0, NOW());

-- 设置表测试数据
INSERT INTO settings (setting_key, setting_value)
VALUES ('site_name', 'My Website'),
       ('timezone', 'UTC');
