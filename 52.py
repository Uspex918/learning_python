# url = "http://www.google.com"

# part = url[:]


# print(url)
# print(part)

# mask = "i_t_s_ _a_ _s_e_c_r_e_t_ _w_o_r_d"

# real = mask[::2]

# print(real)

# url = "http://www.google.com"

# domain = url[url.index("www.") + 4 : -4].capitalize()

# print(domain)

vertebrae = "C1, C2, C3, C4, C5, C6, C7"

number_str = vertebrae[1::4]
# number_str = "".join(sim for sim in vertebrae if sim.isdigit())

print(number_str)
