import re
import operator


def remove_non_alphabetic_char(contents):
    contents = re.sub(r'[^a-zA-Z]',' ', contents)
    return split_contents_by_space(contents)


def split_contents_by_space(contents):
    contents = contents.split()
    return contents


def word_counter(contents):
    dict_word_count = {}
    for word in contents:
        if word not in dict_word_count:
            dict_word_count[word] = 1
        else:
            dict_word_count[word] += 1

    return dict(sorted(dict_word_count.items(), key=operator.itemgetter(1), reverse=True)[:10])


content = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lorem mollis aliquam ut porttitor leo a. Augue ut lectus arcu bibendum at varius. Velit ut tortor pretium viverra suspendisse potenti nullam ac tortor. Sollicitudin aliquam ultrices sagittis orci a scelerisque purus. Tellus id interdum velit laoreet id. Cum sociis natoque penatibus et magnis dis. Sociis natoque penatibus et magnis dis parturient. Imperdiet sed euismod nisi porta lorem mollis aliquam ut. Aliquam ut porttitor leo a diam sollicitudin tempor id eu. Faucibus pulvinar elementum integer enim neque volutpat ac tincidunt vitae. Massa sed elementum tempus egestas sed sed risus pretium quam. Venenatis urna cursus eget nunc scelerisque viverra mauris. Amet venenatis urna cursus eget nunc scelerisque viverra mauris. In metus vulputate eu scelerisque felis imperdiet proin fermentum leo. Arcu cursus vitae congue mauris rhoncus aenean vel elit scelerisque.'

content += ' Diam quis enim lobortis scelerisque fermentum dui faucibus. Vel turpis nunc eget lorem dolor sed. Aliquet sagittis id consectetur purus ut faucibus pulvinar. Nascetur ridiculus mus mauris vitae ultricies leo. Purus gravida quis blandit turpis cursus in hac habitasse platea. Faucibus et molestie ac feugiat sed lectus vestibulum mattis. Ornare arcu dui vivamus arcu felis bibendum ut tristique et. Viverra nam libero justo laoreet sit amet cursus. Tortor pretium viverra suspendisse potenti nullam ac tortor vitae purus. Molestie ac feugiat sed lectus vestibulum mattis ullamcorper. Viverra accumsan in nisl nisi scelerisque eu. Vel turpis nunc eget lorem dolor sed viverra. Eu tincidunt tortor aliquam nulla. Mattis enim ut tellus elementum sagittis vitae et leo. Eu augue ut lectus arcu bibendum at varius vel. Fringilla ut morbi tincidunt augue interdum velit. Consectetur a erat nam at lectus urna duis convallis convallis. Enim ut tellus elementum sagittis vitae. Morbi non arcu risus quis varius quam quisque.'

content += 'Cum sociis natoque penatibus et magnis dis parturient. Sagittis purus sit amet volutpat. In nibh mauris cursus mattis. Enim sed faucibus turpis in eu mi bibendum neque. Turpis egestas integer eget aliquet nibh praesent. Tellus id interdum velit laoreet id donec ultrices tincidunt. Ultrices vitae auctor eu augue ut lectus. Quis auctor elit sed vulputate mi. Placerat in egestas erat imperdiet sed euismod nisi porta. Tristique magna sit amet purus. Massa sed elementum tempus egestas. Sed cras ornare arcu dui vivamus arcu felis.'

content += 'Sed egestas egestas fringilla phasellus faucibus scelerisque. Lobortis elementum nibh tellus molestie. Suscipit adipiscing bibendum est ultricies integer. Ornare quam viverra orci sagittis. Scelerisque eu ultrices vitae auctor eu augue ut. Iaculis urna id volutpat lacus laoreet non. Senectus et netus et malesuada fames ac turpis egestas. Urna nunc id cursus metus aliquam. Ac orci phasellus egestas tellus rutrum tellus. Erat velit scelerisque in dictum non consectetur a. Quis viverra nibh cras pulvinar mattis nunc. Lacus viverra vitae congue eu consequat. Accumsan sit amet nulla facilisi. Amet venenatis urna cursus eget nunc scelerisque viverra mauris in. Tincidunt nunc pulvinar sapien et ligula ullamcorper. Quam lacus suspendisse faucibus interdum posuere lorem. Felis eget velit aliquet sagittis id. Nullam non nisi est sit amet facilisis magna etiam.'

content += 'Pharetra magna ac placerat vestibulum lectus mauris ultrices eros. Imperdiet massa tincidunt nunc pulvinar sapien et ligula. Auctor elit sed vulputate mi sit amet mauris commodo quis. Viverra vitae congue eu consequat ac felis donec. At tellus at urna condimentum mattis pellentesque id nibh tortor. Rhoncus aenean vel elit scelerisque mauris pellentesque pulvinar pellentesque habitant. Nascetur ridiculus mus mauris vitae ultricies leo integer malesuada. Massa massa ultricies mi quis hendrerit dolor magna. Rhoncus aenean vel elit scelerisque mauris. Nunc aliquet bibendum enim facilisis gravida neque convallis a cras.'

content += 'Odio ut enim blandit volutpat maecenas volutpat. Etiam sit amet nisl purus in mollis nunc sed id. Felis imperdiet proin fermentum leo vel. Morbi tristique senectus et netus et malesuada fames ac. At volutpat diam ut venenatis tellus in. In nibh mauris cursus mattis molestie a iaculis. Vulputate mi sit amet mauris commodo quis. Massa sapien faucibus et molestie ac feugiat. Commodo viverra maecenas accumsan lacus vel facilisis volutpat. Et malesuada fames ac turpis egestas maecenas pharetra convallis posuere.'

content += 'Risus feugiat in ante metus dictum at tempor commodo. Accumsan in nisl nisi scelerisque eu. Quam pellentesque nec nam aliquam sem et. Eu facilisis sed odio morbi quis commodo odio aenean sed. Viverra mauris in aliquam sem fringilla. Amet porttitor eget dolor morbi non arcu. Velit aliquet sagittis id consectetur purus ut faucibus. Est pellentesque elit ullamcorper dignissim. Tortor id aliquet lectus proin. Nullam eget felis eget nunc lobortis mattis. In mollis nunc sed id semper. Euismod lacinia at quis risus sed vulputate odio ut. Donec massa sapien faucibus et molestie ac feugiat. Sed adipiscing diam donec adipiscing tristique risus nec. At auctor urna nunc id cursus. Egestas dui id ornare arcu odio. Amet luctus venenatis lectus magna fringilla. Tempus urna et pharetra pharetra. Enim ut tellus elementum sagittis vitae et leo duis ut. Curabitur gravida arcu ac tortor dignissim convallis aenean et.'

content += 'Elit scelerisque mauris pellentesque pulvinar pellentesque habitant morbi. Pharetra vel turpis nunc eget. Phasellus egestas tellus rutrum tellus pellentesque eu tincidunt tortor aliquam. Quis varius quam quisque id. Id aliquet risus feugiat in ante metus dictum at tempor. Vestibulum morbi blandit cursus risus at ultrices mi tempus. Sed viverra tellus in hac habitasse platea. Et pharetra pharetra massa massa ultricies mi. Pellentesque dignissim enim sit amet. Tortor at risus viverra adipiscing at. Amet risus nullam eget felis eget. Cum sociis natoque penatibus et magnis. Convallis tellus id interdum velit laoreet id. Ornare arcu dui vivamus arcu felis bibendum. Luctus accumsan tortor posuere ac ut consequat semper. Ultrices dui sapien eget mi proin sed libero. Amet mauris commodo quis imperdiet massa tincidunt. Faucibus vitae aliquet nec ullamcorper sit amet risus. Elementum tempus egestas sed sed. Adipiscing tristique risus nec feugiat in fermentum posuere urna nec.'

content += 'Purus sit amet luctus venenatis lectus magna fringilla urna porttitor. Id cursus metus aliquam eleifend mi in nulla posuere. Adipiscing bibendum est ultricies integer. Viverra nam libero justo laoreet sit amet. Auctor eu augue ut lectus arcu. Mauris augue neque gravida in fermentum et. Diam sollicitudin tempor id eu nisl nunc. Mollis nunc sed id semper risus in. Leo duis ut diam quam nulla. Mus mauris vitae ultricies leo integer malesuada nunc vel. Aliquet nibh praesent tristique magna sit amet purus gravida. Vitae congue eu consequat ac felis donec et odio.'

content += 'Fusce ut placerat orci nulla. Dictum varius duis at consectetur lorem donec massa sapien faucibus. Cras sed felis eget velit aliquet sagittis id consectetur. Nibh praesent tristique magna sit amet purus gravida quis blandit. Aliquam sem fringilla ut morbi tincidunt. Arcu dui vivamus arcu felis bibendum ut tristique et. Commodo nulla facilisi nullam vehicula. Interdum varius sit amet mattis vulputate enim. Sit amet tellus cras adipiscing enim eu turpis. Leo vel orci porta non pulvinar neque laoreet suspendisse interdum. Et egestas quis ipsum suspendisse ultrices gravida dictum. Enim nulla aliquet porttitor lacus luctus accumsan tortor posuere ac. Pretium quam vulputate dignissim suspendisse. Egestas maecenas pharetra convallis posuere morbi leo urna molestie.'
print(content)
content = remove_non_alphabetic_char(content)
print(word_counter(content))