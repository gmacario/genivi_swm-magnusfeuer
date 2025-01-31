# (c) 2015 - Jaguar Land Rover.
#
# Mozilla Public License 2.0
#
# Python-based partition manager PoC



import gtk
import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop
import sys
import time
import swm

#
# Partition manager service
#
class PartMgrService(dbus.service.Object):
    def __init__(self):
        bus_name = dbus.service.BusName('org.genivi.partition_manager', bus=dbus.SessionBus())
        dbus.service.Object.__init__(self, bus_name, '/org/genivi/partition_manager')


    @dbus.service.method('org.genivi.partition_manager',
                         async_callbacks=('send_reply', 'send_error'))
    def create_disk_partition(self, 
                              transaction_id,
                              disk,
                              partition_number,
                              partition_type,
                              start,
                              size,
                              guid,
                              name,
                              send_reply, 
                              send_error): 

        print "Partition Manager: create_disk_partition()"
        print "  Operfation Transaction ID: {}".format(transaction_id)
        print "  Disk:                      {}".format(disk)
        print "  Partition Number:          {}".format(partition_number)
        print "  Partition Type:            {}".format(partition_type)
        print "  Start:                     {}".format(start)
        print "  Size:                      {}".format(size)
        print "  GUID:                      {}".format(guid)
        print "  Name:                      {}".format(name)
        print "---"

        #
        # Send back an immediate reply since DBUS
        # doesn't like python dbus-invoked methods to do 
        # their own calls (nested calls).
        #
        send_reply(True)

        # Simulate install
        print "Create partition: disk({}) partiton({}) (3 sec)".format(disk, partition_number)
        for i in xrange(1,30):
            sys.stdout.write('.')
            sys.stdout.flush()
            time.sleep(0.1)
        print  
        print "Done"
        swm.send_operation_result(transaction_id,
                                  swm.SWM_RES_OK,
                                  "Partition create successful. Disk: {}:{}".format(disk, partition_number))

        return None
                 

    @dbus.service.method('org.genivi.partition_manager',
                         async_callbacks=('send_reply', 'send_error'))
    def resize_disk_partition(self, 
                              transaction_id,
                              disk,
                              partition_number,
                              start,
                              size,
                              send_reply, 
                              send_error): 

        print "Partition Manager: resize_disk_partition()"
        print "  Operfation Transaction ID: {}".format(transaction_id)
        print "  Disk:                      {}".format(disk)
        print "  Partition Number:          {}".format(partition_number)
        print "  Start:                     {}".format(start)
        print "  Size:                      {}".format(size)
        print "---"

        #
        # Send back an immediate reply since DBUS
        # doesn't like python dbus-invoked methods to do 
        # their own calls (nested calls).
        #
        send_reply(True)

        # Simulate install
        print "Resizing partition: disk({}) partiton({}) (10 sec)".format(disk, partition_number)
        for i in xrange(1,50):
            sys.stdout.write('.')
            sys.stdout.flush()
            time.sleep(0.2)
        print  
        print "Done"
        swm.send_operation_result(transaction_id,
                                   swm.SWM_RES_OK,
                                   "Partition resize success. Disk: {}:{}".format(disk, partition_number))
        return None


    @dbus.service.method('org.genivi.partition_manager',
                         async_callbacks=('send_reply', 'send_error'))
    def delete_disk_partition(self, 
                              transaction_id,
                              disk,
                              send_reply, 
                              send_error): 

        print "Partition Manager: delete_disk_partition()"
        print "  Operfation Transaction ID: {}".format(transaction_id)
        print "  Disk:                      {}".format(disk)
        print "  Partition Number:          {}".format(partition_number)
        print "---"

        #
        # Send back an immediate reply since DBUS
        # doesn't like python dbus-invoked methods to do 
        # their own calls (nested calls).
        #
        send_reply(True)

        # Simulate install
        print "Delete partition: disk({}) partiton({}) (5 sec)".format(disk, partition_number)
        for i in xrange(1,10):
            sys.stdout.write('.')
            sys.stdout.flush()
            time.sleep(0.2)
        print  
        print "Done"
        swm.send_operation_result(transaction_id,
                                   swm.SWM_RES_OK,
                                   "Partition delete success. Disk: {}:{}".format(disk, partition_number))

        return None


    @dbus.service.method('org.genivi.partition_manager',
                         async_callbacks=('send_reply', 'send_error'))
    def write_disk_partition(self, 
                             transaction_id,
                             disk,
                             partition_number,
                             image_path,
                             blacklisted_partitions,
                             send_reply, 
                             send_error): 

        print "Partition Manager: write_disk_partition()"
        print "  Operfation Transaction ID: {}".format(transaction_id)
        print "  Disk:                      {}".format(disk)
        print "  Partition Number:          {}".format(partition_number)
        print "  Image Path:                {}".format(image_path)
        print "  Blacklisted Partitions:    {}".format(blacklisted_partitions)
        print "---"

        #
        # Send back an immediate reply since DBUS
        # doesn't like python dbus-invoked methods to do 
        # their own calls (nested calls).
        #
        send_reply(True)

        # Simulate write
        print "Writing partition: disk({}) partiton({}) (10 sec)".format(disk, partition_number)
        for i in xrange(1,50):
            sys.stdout.write('.')
            sys.stdout.flush()
            time.sleep(0.2)
        print  
        print "Done"
        swm.send_operation_result(transaction_id,
                                  swm.SWM_RES_OK,
                                  "Partition write success. Disk: {}:{} Image: {}".
                                  format(disk, partition_number, image_path))

        return None
                 

    @dbus.service.method('org.genivi.partition_manager',
                         async_callbacks=('send_reply', 'send_error'))
    def patch_disk_partition(self, 
                             transaction_id,
                             disk,
                             partition_number,
                             image_path,
                             blacklisted_partitions,
                             send_reply, 
                             send_error): 

        print "Partition Manager: patch_disk_partition()"
        print "  Operfation Transaction ID: {}".format(transaction_id)
        print "  Disk:                      {}".format(disk)
        print "  Partition Number:          {}".format(partition_number)
        print "  Image Path:                {}".format(image_path)
        print "  Blacklisted Partitions:    {}".format(blacklisted_partitions)
        print "---"

        #
        # Send back an immediate reply since DBUS
        # doesn't like python dbus-invoked methods to do 
        # their own calls (nested calls).
        #
        send_reply(True)

        # Simulate patch
        print "Patching partition: disk({}) partiton({}) (10 sec)".format(disk, partition_number)
        for i in xrange(1,50):
            sys.stdout.patch('.')
            sys.stdout.flush()
            time.sleep(0.2)
        print  
        print "Done"
        swm.send_operation_result(transaction_id,
                                  swm.SWM_RES_OK,
                                  "Partition patch success. Disk: {}:{} Image: {}".
                                  format(disk, partition_number, image_path))
        return None
                 

print 
print "Partition Manager."
print
DBusGMainLoop(set_as_default=True)
part_mgr = PartMgrService()

while True:
    gtk.main_iteration()
