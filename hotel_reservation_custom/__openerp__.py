# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    John W. Viloria Amaris <john.viloria.amaris@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name":"Hotel Reservation Customizations",
    "description":"""\
Hotel Reservation Customizations
==================================

Module for guest reservation adjusting.
    """,
    "depends":["hotel_partner","hotel_custom"],
    "category":"Hotel Management",
    "author":"John Viloria Amaris",
    "data":[
        "views/hotel_reservation_view.xml",
        "views/room_summary_view.xml",
        "data/hotel_summary_data.xml",
        "views/hotel_room_maintenance_view.xml",
    ],
    "qweb": ["static/src/xml/*.xml"],
    "installable":True
 }
