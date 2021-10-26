# importing the required modules
import os
import shutil
import time

# main function
def main():

	# initializing the count
	deleted_folders_count = 0
	deleted_files_count = 0

	# specify the path
	path = "/PATH_TO_DELETE"

	# specify the days
	days = 30

	# converting days to seconds
	# time.time() returns current time in seconds
	seconds = time.time() - (days * 24 * 60 * 60)

	# checking whether the file is present in path or not
	if os.path.exists(path):

		# iterating over each and every folder and file in the path
		for root_folder, folders, files in os.walk(path):

			# comparing the days
			if seconds >= get_file_or_folder_age(root_folder):

				# removing the folder
				remove_folder(root_folder)
				deleted_folders_count += 1 # incrementing count

				# breaking after removing the root_folder
				break

			else:

				# checking folder from the root_folder
				for folder in folders:

					# folder path
					folder_path = os.path.join(root_folder, folder)

					# comparing with the days
					if seconds >= get_file_or_folder_age(folder_path):

						# invoking the remove_folder function
						remove_folder(folder_path)
						deleted_folders_count += 1 # incrementing count


				# checking the current directory files
				for file in files:

					# file path
					file_path = os.path.join(root_folder, file)

					# comparing the days
					if seconds >= get_file_or_folder_age(file_path):

						# invoking the remove_file function
						remove_file(file_path)
						deleted_files_count += 1 # incrementing count

		else:

			# if the path is not a directory
			# comparing with the days
			if seconds >= get_file_or_folder_age(path):

				# invoking the file
				remove_file(path)
				deleted_files_count += 1 # incrementing count

	else:

		# file/folder is not found
		print(f'"{path}" is not found')
		deleted_files_count += 1 # incrementing count

	print(f"Total folders deleted: {deleted_folders_count}")
	print(f"Total files deleted: {deleted_files_count}")


def remove_folder(path):

	# removing the folder
	if not shutil.rmtree(path):

		# success message
		print(f"{path} is removed successfully")

	else:

		# failure message
		print(f"Unable to delete the "+path)



def remove_file(path):

	# removing the file
	if not os.remove(path):

		# success message
		print(f"{path} is removed successfully")

	else:

		# failure message
		print("Unable to delete the "+path)


def get_file_or_folder_age(path):

	# getting ctime of the file/folder
	# time will be in seconds
	ctime = os.stat(path).st_ctime

	# returning the time
	return ctime


if __name__ == '__main__':
	main()
