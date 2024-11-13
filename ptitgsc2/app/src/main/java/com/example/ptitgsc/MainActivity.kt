package com.example.ptitgsc

import android.annotation.SuppressLint
import android.net.Uri
import android.os.Bundle
import android.widget.Button
import android.widget.MediaController
import android.widget.Toast
import android.widget.VideoView
import androidx.appcompat.app.AppCompatActivity
import com.google.android.gms.maps.CameraUpdateFactory
import com.google.android.gms.maps.GoogleMap
import com.google.android.gms.maps.OnMapReadyCallback
import com.google.android.gms.maps.SupportMapFragment
import com.google.android.gms.maps.model.BitmapDescriptorFactory
import com.google.android.gms.maps.model.LatLng
import com.google.android.gms.maps.model.MarkerOptions
import com.google.firebase.database.*
import com.google.firebase.firestore.*


var check_full_data = false
var cnt=0
var db = FirebaseDatabase.getInstance().reference
var dec_list = mutableListOf<Decv>()
class MainActivity : AppCompatActivity(), OnMapReadyCallback {

    @SuppressLint("MissingInflatedId")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        val updateBtn: Button = findViewById(R.id.button)

        val mapFragment = supportFragmentManager
            .findFragmentById(R.id.map) as SupportMapFragment?
        mapFragment!!.getMapAsync(this)



        val videoView = findViewById<VideoView>(R.id.videoView)

        // Set up media controller
        val mediaController = MediaController(this)
        mediaController.setAnchorView(videoView)
        videoView.setMediaController(mediaController)

        // Set up video URI
        val videoUri = Uri.parse("rtsp://r.c2ha.com:8554/mystream")

        // Set up video view
        videoView.setVideoURI(videoUri)
        videoView.requestFocus()
        videoView.start()

        var check = true

        var resetBtn: Button = findViewById(R.id.button2)
        resetBtn.setOnClickListener {
            db.child("fly").child("cnt").setValue(0);
            cnt = 0
            check_full_data = false
        }
        updateBtn.setOnClickListener {

            db.child("fly").get().addOnSuccessListener {
                check = it.child("bool").value as Boolean
                db.child("fly").child("bool").setValue(true);
                Toast.makeText(this, "Update location", Toast.LENGTH_SHORT).show()
                cnt++
                if (cnt == 3) check_full_data = true
                if (cnt < 4) {
                    db.child("fly").child("cnt").setValue(cnt);
                }

            }
        }

    }

    override fun onMapReady(googleMap: GoogleMap) {
        var mMap = googleMap

        db.child("fly").addValueEventListener(object : ValueEventListener {
            override fun onDataChange(snapshot: DataSnapshot) {
                if (snapshot.exists()) {
//                      Location 3 of flycam
                        val lat_fly_1: String = snapshot.child("loc_1").child("lat").value.toString()
                        val lng_fly_1: String = snapshot.child("loc_1").child("lon").value.toString()
                        val latitude_fly_1 = lat_fly_1.toDouble()
                        val longitude_fly_1 = lng_fly_1.toDouble()
                        val loc_fly_1 = LatLng(latitude_fly_1, longitude_fly_1)

                        val mMarker_1 = googleMap.addMarker(
                            MarkerOptions().position(loc_fly_1)
                                .title("Fly_1")
                        )
                        mMap.moveCamera(CameraUpdateFactory.newLatLngZoom(loc_fly_1, 14.0f));
//                  Location 2 of flycam
                    val lat_fly_2: String = snapshot.child("loc_2").child("lat").value.toString()
                    val lng_fly_2: String = snapshot.child("loc_2").child("lon").value.toString()
                    val latitude_fly_2 = lat_fly_2.toDouble()
                    val longitude_fly_2 = lng_fly_2.toDouble()
                    val loc_fly_2 = LatLng(latitude_fly_2, longitude_fly_2)

                    val mMarke_2 = googleMap.addMarker(
                        MarkerOptions().position(loc_fly_2)
                            .title("Fly_2")
                    )
//                  Location 3 of flycam
                    val lat_fly_3: String = snapshot.child("loc_3").child("lat").value.toString()
                    val lng_fly_3: String = snapshot.child("loc_3").child("lon").value.toString()
                    val latitude_fly_3 = lat_fly_3.toDouble()
                    val longitude_fly_3 = lng_fly_3.toDouble()
                    val loc_fly_3 = LatLng(latitude_fly_3, longitude_fly_3)

                    val mMarker_3 = googleMap.addMarker(
                        MarkerOptions().position(loc_fly_1)
                            .title("Fly_3")
                    )

                }
            }

            override fun onCancelled(error: DatabaseError) {

            }
        })
            db.child("device").addValueEventListener(object : ValueEventListener {
                override fun onDataChange(snapshot: DataSnapshot) {
                    if (snapshot.exists()) {
                        for (missionSnapshot in snapshot.children) {
                            val lat: String = missionSnapshot.child("lat").value.toString()
                            val lng: String = missionSnapshot.child("lon").value.toString()
                            val latitude = lat.toDouble()
                            val longitude = lng.toDouble()
                            val loc = LatLng(latitude, longitude)
                            val idMission = missionSnapshot.child("mac_addr").value.toString()

                            val mMarker = googleMap.addMarker(
                                MarkerOptions().position(loc)
                                    .title(idMission)
                            )

                        }
                    }
                }

                override fun onCancelled(error: DatabaseError) {

                }
            })


        }

}
