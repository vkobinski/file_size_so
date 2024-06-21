use std::{
    fs::{self, DirEntry, File},
    io::Write,
    os::unix::fs::MetadataExt,
    path::Path,
    process::Command,
    time::Instant,
};

fn visit_dirs(dir: &Path, file_sizes: &mut File) {
    for entry in fs::read_dir(dir).unwrap() {
        let entry = entry.unwrap();

        let file_size = entry.metadata().unwrap().size();

        let _ = file_sizes.write(
            format!(
                "{}: {}\n",
                entry.file_name().into_string().unwrap(),
                file_size
            )
            .as_bytes(),
        );

        let path = entry.path();
        if path.is_dir() {
            visit_dirs(&path, file_sizes);
        }
    }
}
fn main() {
    let mut file_sizes = File::create("./sizes.txt").unwrap();
    visit_dirs(Path::new("/home/vkobinski/projects"), &mut file_sizes);
}
