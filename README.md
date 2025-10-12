  <header style="border-bottom:1px solid #e6e6e6; padding-bottom:12px; margin-bottom:20px;">
    <h1 style="font-size:1.6rem; margin:0;">Kana Fotilo: Ραβδί για υποβοηθούμενη κατεύθυνση</h1>
    <p style="color:#6b7280; margin:6px 0 0 0;">Project της IEEE UNIWA</p>
  </header>

  <section style="background:#fbfbff; border:1px solid #eef2ff; padding:16px; border-radius:10px; box-shadow:0 6px 18px rgba(11,103,255,0.04);">
    <h2 style="margin-top:0;">Περίληψη</h2>
    <p style="margin:0.5rem 0;">Το <strong>Kana Fotilo</strong> είναι ένα ραβδί που θα επιτρέπει σε άτομα με ελάχιστη ικανότητα όρασης να μετακινηθούν στο χώρο χωρίς βοήθεια. Οι ψηφιακοί αισθητήρες που περιέχει, σε συνδυασμό με το σχεδιασμό του σαν κλασσικό ραβδί, επιτρέπουν στον χρήστη να περιηγηθεί στο χώρο αυτόνομα.</p>
  </section>

  <section style="margin-top:16px;">
    <h2 style="margin-bottom:8px;">Λειτουργία</h2>
    <ol style="margin:0.5rem 0 0 1.25rem;">
      <li>Ο αισθητήρας σαρώνει τον χώρο σε τομείς.</li>
      <li>Οι μετρήσεις αποθηκεύονται σε πίνακα και αναλύονται.</li>
      <li>Αν εντοπιστεί εμπόδιο, το σύστημα επιλέγει ασφαλή κατεύθυνση.</li>
      <li>Το <code style="background:#f3f4f6; padding:2px 6px; border-radius:6px;">servo</code> στρέφει το ραβδί προς την κατάλληλη πορεία.</li>
      <li>Ο <code style="background:#f3f4f6; padding:2px 6px; border-radius:6px;">buzzer</code> ή/και το ηχείο ειδοποιούν τον χρήστη.</li>
    </ol>
  </section>

  <section style="margin-top:12px;">
    <h2 style="margin-bottom:8px;">Χαρακτηριστικά</h2>
    <div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(220px,1fr)); gap:12px; margin-top:12px;">
      <div style="padding:12px; border-radius:8px; border:1px solid #f0f0f0; background:#fff;">
        <strong>Αισθητήρες</strong>
        <p style="margin:6px 0 0 0;">Υπέρηχος / LIDAR / ToF — Ανίχνευση εμποδίων σε διαφορετικά ύψη.</p>
      </div>
      <div style="padding:12px; border-radius:8px; border:1px solid #f0f0f0; background:#fff;">
        <strong>Servo Motor</strong>
        <p style="margin:6px 0 0 0;">Κατεύθυνση του χρήστη προς ασφαλές μονοπάτι.</p>
      </div>
      <div style="padding:12px; border-radius:8px; border:1px solid #f0f0f0; background:#fff;">
        <strong>Buzzer & Ηχείο</strong>
        <p style="margin:6px 0 0 0;">Ηχητικές ειδοποιήσεις και φωνητική καθοδήγηση.</p>
      </div>
      <div style="padding:12px; border-radius:8px; border:1px solid #f0f0f0; background:#fff;">
        <strong>IMU & GPS</strong>
        <p style="margin:6px 0 0 0;">Καθοδήγηση σε εξωτερικό χώρο.</p>
      </div>
      <div style="padding:12px; border-radius:8px; border:1px solid #f0f0f0; background:#fff;">
        <strong>Εφαρμογή</strong>
        <p style="margin:6px 0 0 0;">Ρύθμιση προορισμού μέσω OpenStreetMap API.</p>
      </div>
    </div>
  </section>

  <footer style="border-top:1px solid #e6e6e6; margin-top:22px; padding-top:12px; color:#6b7280; font-size:0.95rem;">
    <p style="margin:0;">Project της IEEE UniWA, biomed sg. Για περισσοτερες λεπτομέρειες επισκεφτείτε το <a href = "https://github.com/PaulosKapa/kana_fotilo/wiki" target = "_blank">wiki</a></p>
  </footer>

