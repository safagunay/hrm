from depot.manager import DepotManager

DepotManager.configure('default', {
    'depot.storage_path': './files'
})
print(DepotManager.get_default())
print(DepotManager.get())
depot = DepotManager.get()
fileid = depot.create(open('./testfiles/fake.txt','br'))
stored_file = depot.get(fileid)
print(stored_file.content_type)