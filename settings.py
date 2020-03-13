

save_directory = os.path.realpath('dataset')

# the name of your dataset

output_file = os.path.join(save_directory, 'custom_dataset.csv')

# where you store your source files

crawl_from = 'C:/Users/oracle/desktop/projects'

# label to describe the file extension

labels = {'php': 'php', 'py': 'python'}


# do not edit the line below!

# do not edit the line below!

# do not edit the line below!

# do not edit the line below!


keywords = ['true', '<mark>', 'function', '<fieldset>', '<object>', 'template', '<tbody>', '__FILE__', 'as', '<address>', '<td>', 'volatile', '<var>', 'nonlocal', '<progress>', 'endforeach', '<rtc>', '<template>', 'typeid', '<tr>', 'bool', '<table>', '<track>', '<dt>', 'import', 'continue', 'from', 'return', '<option>', 'struct', '<header>', 'lambda', 'print', 'reinterpret_cast', 'E_WARNING', 'PHP_VERSION', 'echo', '<param>', 'unsigned', '<wbr>', 'FALSE', 'endswitch', 'rethrow', 'is', '<main>', '<samp>', 'double', 'switch', '<tfoot>', '<dl>', '<base>', 'extern', 'include', 'argv', 'del', '<time>', 'void', '<col>', 'PHP_OS', 'short', 'except', 'namespace',
            'pass', 'if', 'for', 'foreach', 'in', 'default', '<dfn>', '<p>', '<dd>', '<style>', 'HTTP_GET_VARS', 'operator', '<rt>', 'false', 'include_once', 'HTTP_ENV_VARS', 'global', 'sync', 'typedef', 'null', 'throw', 'names', 'library', 'int', 'HTTP_SERVER_VARS', '<blockquote>', '<iframe>', 'with', 'def', '<optgroup>', '<script>', '<kbd>', 'set', 'do', '__LINE__', 'NULL', '<embed>', '<audio>', 'case', 'implements', 'static_cast', 'mutable', 'signed', '<datalist>', 'TRUE', '<ruby>', '<u>', '<colgroup>', '<th>', '<span>', 'sizeof',
            'HTTP_COOKIE_VARS', 'get', '<article>', '<label>', 'friend', '<li>', '<abbr>', '<rp>', 'else', 'dynamic_cast', '<area>', '<input>',
            'die', '<link>', 'elseif', '<body>', 'typename', '<figcaption>', 'factory', 'virtual', '<meter>', '<legend>', 'static', '__sleep', 'final', 'export', 'class', '<pre>', '<video>', 'empty', '<i>', '<meta>', '<html>', 'wchar_t', 'try', '<canvas>', '<img>', 'part', '<button>', '<textarea>', 'dynamic', 'float', 'inline', 'abstract', '<footer>', '<b>', 'endwhile', '<bdi>', 'E_PARSE', '<head>', 'PHP_SELF', 'enum', 'long', '<ins>', 'stdClass', 'char', 'const_cast', 'E_ALL', 'this', 'var', 'await', '<div>', 'HTTP_POST_FILES', 'None', '__wakeup', 'or', '<a>', '<data>', 'not', 'elif', '<thead>', '<hr>', 'endif', 'list', '<source>', 'yield', 'E_ERROR', '<rb>', '<figure>', 'catch', 'public', '<del>', 'while', '<caption>', '<h1>', 'require_once', '<q>', 'private', 'auto', 'goto', 'async', 'new', '<output>', '<small>', 'deferred', '<aside>', '<section>', '<select>', '<sub>', '<ol>', 'and', 'endfor', 'xor', 'union', 'explicit', '<cite>', '<code>', '<em>', '<title>', 'finally', '<ul>', 'delete', '<strong>', '<nav>', '<br>', 'const', 'argc', 'assert', 'parent', 'asm', 'require', '<bdo>', '<form>', 'False', '<keygen>', '<s>', '<sup>', 'external', 'raise', 'exit', 'extends', 'protected', 'using', 'break', 'super', 'True', 'HTTP_POST_VARS', '<map>', 'register', '<h6>', '<noscript>']
