acc_info={"aakash":72834688934, "harish":7897348973, "aaditya":97897723987}

# Print all dict keys
keys=acc_info.keys()
print("keys=>",keys)

# Print all dict values
# option 1, gadha hemali
print('Value=>', acc_info['aakash'])

# option 2 acc_info[key] and acc_info.get(key)
for key in keys:
    if key == 'aaditya':
        del acc_info['aaditya']
    print('Value=>', acc_info[key])
    acc_info[key] = acc_info[key] + 1

print('after update', acc_info)

