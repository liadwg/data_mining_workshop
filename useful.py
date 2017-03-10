
#group by
tips = all_data.groupby(['price_range'], as_index=False).count()[['price_range', 'likes']]
all_data.groupby(['search_category'], as_index=False).mean()[['search_category','likes']]
df.groupby(key_columns).size() #count

#sort
bla.sort_values('likes', ascending=False)

#filter


#rename
tips.rename(columns={'likes':'cnt'}, inplace=True)
all_data.price_range.map({0:'None', 1:'1$', 2:'2$', 3:'3$', 4:'4$'})


all_data[all_data['has_profile_photo'] < 1].shape[0]

has_columns = [a for a in all_data.columns.get_values() if 'has' in a]

all_data.columns.get_values()
