import math
from particles_and_nuclei import dict_particles

light_particle_in = input(("light_particle = "))
target_particle = input(("target = "))
light_particle_out = input(("light_particle_out = "))
heavy_particle_out = input(("heavy_particle_out = "))

light_particle_mass_in = dict_particles[light_particle_in]["mass"]
target_particle_mass_in = dict_particles[target_particle]["mass"]
light_particle_mass_out = dict_particles[light_particle_out]["mass"]
heavy_particle_mass_out = dict_particles[heavy_particle_out]["mass"]

E_beam = float(input(("Energy_of_the_beam = ")))

Energy_light_particle_cms = []
Energy_heavy_particle_cms = []
E_t = []
A14 = []
A13 = []
A23 = []
A24 = []
degree = [50.0, 51.2, 52.5, 53.9, 55.2, 56.5]


Q_react = dict_particles[target_particle]["Ex_Energy"]["Ex_Energy"].copy()
for i in range(len(dict_particles[target_particle]["Ex_Energy"]["Ex_Energy"])):
    Q_react[i] = 0.0 - Q_react[i]
    E_t.append(E_beam + Q_react[i])
    A14.append((light_particle_mass_in*heavy_particle_mass_out)*(E_beam/E_t[i])/((light_particle_mass_in+target_particle_mass_in)*(light_particle_mass_out+heavy_particle_mass_out)))
    A13.append((light_particle_mass_in*light_particle_mass_out)*(E_beam/E_t[i])/((light_particle_mass_in+target_particle_mass_in)*(light_particle_mass_out+heavy_particle_mass_out)))
    A23.append(((target_particle_mass_in*light_particle_mass_out)/((light_particle_mass_in+target_particle_mass_in)*(light_particle_mass_out+heavy_particle_mass_out)))*(1.0+(light_particle_mass_in*Q_react[i]/(target_particle_mass_in*E_t[i]))))
    A24.append(((target_particle_mass_in*heavy_particle_mass_out)/((light_particle_mass_in+target_particle_mass_in)*(light_particle_mass_out+heavy_particle_mass_out)))*(1.0+(light_particle_mass_in*Q_react[i]/(target_particle_mass_in*E_t[i]))))
    Energy_light_particle_cms.append(A24[i] * E_t[i])
    Energy_heavy_particle_cms.append(A23[i] * E_t[i])

E3_light = []
sin_cm = []
degree_cm = []

for k in range(len(degree)):
    for i in range(len(Q_react)):
        E3_Et = A13[i]*(math.cos(degree[k]*math.pi/180) + ((A24[i]/A13[i]) - math.sin(degree[k]*math.pi/180)**2)**(0.5))**2
        E3_light.append(E3_Et * E_t[i])
        sin_cm = ((E3_Et/A24[i])**(0.5))*math.sin(degree[k]*math.pi/180)
        degree_cm.append(math.asin(sin_cm)*180/math.pi)
        #print("Degree_lab", "Degree_cm", "Ex", "E_light")
        print(degree[k], degree_cm[i], 0.0 - Q_react[i], E3_light[i])

print(E3_light)
Enetgy_light_particle_position_cms = []




#print(Energy_light_particle_cms)
#print(math.cos(60 * math.pi/180))







