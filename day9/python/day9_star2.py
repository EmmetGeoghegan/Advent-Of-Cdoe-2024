
class DriveSector:
    all_sectors_in_order = []
    all_storage_in_order = []
    all_gaps_in_order = []


    def __init__(self, sector_id, sector_length, sector_type):
        self.sector_id = sector_id
        self.sector_id_int = int(sector_id)
        self.sector_length = sector_length
        self.sector_type = sector_type

        if self.sector_type == "Storage":
            self.storage = []
            DriveSector.all_gaps_in_order.append(self)
        else:
            self.storage = [self] * self.sector_length
            DriveSector.all_storage_in_order.append(self)

        DriveSector.all_sectors_in_order.append(self)

    def __repr__(self):
        if self.sector_type == "Storage":
            if self.sector_length:
                return "-" + "".join([i.sector_id for i in self.storage]) + "." * (self.sector_length - len(self.storage)) + "-" + self.sector_type
            return "-" + "." * self.sector_length + "-" + self.sector_type
        return "-" + "".join([i.sector_id for i in self.storage]) + "-" + self.sector_type

    def store_data(self, move_sector):
        remaining_capacity = self.sector_length - len(self.storage)
        needed_capacity = len(move_sector.storage)

        self.storage += [move_sector] * min(remaining_capacity, needed_capacity)

        if len(self.storage) == self.sector_length:
            self.sector_type = "Data"

        move_sector.release_space(min(remaining_capacity, needed_capacity))

    def release_space(self, space_released):
        # print("Storage before:", self.storage)
        del self.storage[-space_released:]
        # print("Storage after:", self.storage, space_released)
        if len(self.storage) == 0:
            self.sector_type = "Storage"
            DriveSector.all_gaps_in_order.append(self)



with open("input.txt", "r") as disk_file:
    disk_data = disk_file.readline()

data_id = 0
for i in range(0, len(disk_data)):
    if i % 2 == 0:
        # Data sector
        # print(f"DATA - {data_id} - length:{disk_data[i]}")
        DriveSector(str(data_id), int(disk_data[i]), sector_type="Data")
        data_id += 1
    else:
        # free space sector
        # print(f"FREE SPACE - length:{disk_data[i]}")
        if disk_data[i] != "0":
            DriveSector(str(-1), int(disk_data[i]), sector_type="Storage")
        else:
            print("storage skipped")


# for i in DriveSector.all_sectors_in_order:
#     print(i)


while True:
    move_sector = DriveSector.all_storage_in_order.pop()
    # print("MOVING:",move_sector)

    space_required = len(move_sector.storage)
    # print("SPACE REQUIRED:", space_required)

    while True:
        # Loop through available storage sectors - If => storage needed move the file
        if len(DriveSector.all_gaps_in_order) > 0:
            gap_sector = DriveSector.all_gaps_in_order.pop(0)
            gap_sector_capacity = gap_sector.sector_length - len(gap_sector.storage)
            # print("Gap capacity:", gap_sector_capacity)

            if gap_sector_capacity > space_required:
                gap_sector.store_data(move_sector)
                DriveSector.all_gaps_in_order.insert(0, gap_sector)
                break

            elif gap_sector_capacity == space_required:
                gap_sector.store_data(move_sector)
                break

            else:
                gap_sector.store_data(move_sector)
                DriveSector.all_storage_in_order.append(move_sector)
                break
        else:
            print("Shouldnt happen - out of storage")


    # print("============")
    # for i in DriveSector.all_sectors_in_order:
    #     print(i)
    # print("------------")
    # print([i for i in DriveSector.all_gaps_in_order])
    # print([i for i in DriveSector.all_storage_in_order])
    # print("============")
    exit_flag = [i for i in range(1, len(DriveSector.all_sectors_in_order)) if DriveSector.all_sectors_in_order[i].sector_type != DriveSector.all_sectors_in_order[i-1].sector_type]
    # print(exit_flag)
    if len(exit_flag) == 1:
        break
print("done!")

counter = 0
total = 0
for i in DriveSector.all_sectors_in_order:
    for j in i.storage:
        block_value = counter * j.sector_id_int
        print(j.sector_id_int)
        if j.sector_id_int == -1:
            print("sad")
            exit()

        total += block_value
        counter += 1

print(total)

# 5841612214957 - Too low



