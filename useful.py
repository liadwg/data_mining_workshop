
#group by
tips = all_data.groupby(['price_range'], as_index=False).count()[['price_range', 'likes']]

#rename
tips.rename(columns={'likes':'cnt'}, inplace=True)
all_data.price_range.map({0:'None', 1:'1$', 2:'2$', 3:'3$', 4:'4$'})


all_data[all_data['has_profile_photo'] < 1].shape[0]