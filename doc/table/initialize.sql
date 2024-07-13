-- 用户表
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '用户唯一ID，不重复',
    username VARCHAR(255) NOT NULL COMMENT '用户在系统中展示的名称',
    email VARCHAR(255) NOT NULL COMMENT '用于用户登录的账户',
    password VARCHAR(255) NOT NULL COMMENT '用户登录密码（存储加密过后的密码）',
    code VARCHAR(255) COMMENT '用户注册时创建的验证码',
    avatar VARCHAR(255) COMMENT '用户头像，是一个url链接',
    phone INT COMMENT '用户绑定电话，后期可用于发送信息',
    qq INT COMMENT '用户绑定QQ，后期可用于联系',
    role VARCHAR(255) COMMENT '用户角色，一个泛型，0：普通用户，1：游客，2：管理员',
    create_time TIMESTAMP COMMENT '用户创建时的时间',
    last_login_time TIMESTAMP COMMENT '用户最后登录的时间',
    create_mac VARCHAR(255) COMMENT '用户创建时的MAC地址',
    create_ip VARCHAR(255) COMMENT '用户创建时的IP地址',
    last_login_ip VARCHAR(255) COMMENT '用户最后登录时的IP地址',
    address VARCHAR(255) COMMENT '用户具体居住地址',
    city VARCHAR(255) COMMENT '用户所属城市',
    status INT DEFAULT 0 COMMENT '用户状态，一个泛型，0：未激活，1：激活，2：删除，默认0'
);

-- 分类表
CREATE TABLE IF NOT EXISTS categories (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '分类唯一ID，不可重复',
    content VARCHAR(255) COMMENT '分类内容',
    author_id INT COMMENT '该分类创建者ID，可通过该ID查找到作者',
    status INT DEFAULT 0 COMMENT '分类状态，一个泛型，0：发布，1：隐藏，2：删除（不显示到前端），默认0',
    create_time TIMESTAMP COMMENT '该分类创建时间'
);

-- 标签表
CREATE TABLE IF NOT EXISTS tags (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '标签唯一ID，不可重复',
    content VARCHAR(255) COMMENT '标签内容',
    author_id INT COMMENT '该标签创建者ID，可通过该ID查找到作者',
    status INT DEFAULT 0 COMMENT '标签状态，一个泛型，0：发布，1：隐藏，2：删除（不显示到前端），默认0',
    create_time TIMESTAMP COMMENT '标签创建时间'
);

-- 评论表
CREATE TABLE IF NOT EXISTS comments (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '评论唯一ID，不可重复',
    author_id VARCHAR(255) COMMENT '该评论所属用户ID',
    article_id VARCHAR(255) COMMENT '该评论所属文章的ID',
    father_id VARCHAR(255) COMMENT '该评论所属父级的ID',
    title VARCHAR(255) COMMENT '评论标题',
    content TEXT COMMENT '评论内容',
    like_num INT DEFAULT 0 COMMENT '评论点赞数',
    comment_num INT DEFAULT 0 COMMENT '评论数量',
    create_time TIMESTAMP COMMENT '评论创建时间',
    create_ip VARCHAR(255) COMMENT '评论创建时的IP地址',
    status INT DEFAULT 0 COMMENT '评论状态，一个泛型，0：发布，1：隐藏，2：删除（不显示到前端），默认0',
    auditing_status INT DEFAULT 0 COMMENT '审核状态，一个泛型，0：未审核，1：已审核，默认0',
);

-- 附件表
CREATE TABLE IF NOT EXISTS attachments (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '附件唯一ID，不可重复',
    author_id VARCHAR(255) COMMENT '附件上传者ID',
    network_url VARCHAR(255) COMMENT '外部访问的URL地址',
    local_url VARCHAR(255) COMMENT '存储在本地的地址',
    preview_url VARCHAR(255) COMMENT '文件在外部预览地址',
    size INT COMMENT '附件文件大小，单位KB',
    status INT DEFAULT 0 COMMENT '附件状态，一个泛型，0：发布，1：隐藏，2：删除（不显示到前端），默认0',
    create_time TIMESTAMP COMMENT '附件上传时间',
    create_ip VARCHAR(255) COMMENT '附件上传者IP地址'
);

-- 链接表
CREATE TABLE IF NOT EXISTS links (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '链接唯一ID，不可重复',
    title VARCHAR(255) COMMENT '链接标题',
    content TEXT COMMENT '链接内容',
    author_id VARCHAR(255) COMMENT '该链接创建者ID，可通过该ID查找到作者',
    status INT DEFAULT 0 COMMENT '链接状态，一个泛型，0：发布，1：隐藏，2：删除（不显示到前端），默认0',
    create_time TIMESTAMP COMMENT '链接创建时间'
);

-- 设置表
CREATE TABLE IF NOT EXISTS settings (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '设置项唯一ID，不可重复',
    setting_key VARCHAR(255) NOT NULL UNIQUE COMMENT '设置的键，唯一标识具体的设置项，设置前缀为sys/web分别是系统设置和网站设置',
    setting_value TEXT NOT NULL COMMENT '设置的值，可以存储各种设置项的具体值'
);

-- 插入模板
-- 插入系统设置
INSERT INTO
    settings (setting_key, setting_value)
VALUES
    ('sys_enable_redis', 'true');

-- 插入网站设置
INSERT INTO
    settings (setting_key, setting_value)
VALUES
    ('web_site_title', '我的博客'),
    ('web_site_subtitle', '分享我的生活和技术'),
    ('web_site_url', 'https://www.myblog.com'),
    ('web_enable_email', 'true');

-- 插入邮件发送模板设置
INSERT INTO
    settings (setting_key, setting_value)
VALUES
    (
        'web_email_register_template',
        '<html>...注册邮件模板HTML代码...</html>'
    ),
    (
        'web_email_verification_template',
        '<html>...验证码邮件模板HTML代码...</html>'
    ),
    (
        'web_email_reset_success_template',
        '<html>...密码重置成功邮件模板HTML代码...</html>'
    );